"""迷雾地牢：单文件 Python 文字 RPG。

运行：python mist_dungeon.py（Python 3.9+，仅使用标准库）
输入菜单数字后按 Enter。存档放在本脚本旁边。

阅读顺序：配置数据 → Player → Game 的营地菜单 → explore → battle。
可练习：字典、列表、函数、类、dataclass、随机数、JSON 和文件读写。
"""

import json
import os
import random
from dataclasses import asdict, dataclass, field
from pathlib import Path


SAVE_PATH = Path(__file__).resolve().with_name("mist_dungeon_save.json")
SAVE_VERSION = 1

JOBS = {
    "1": {"name": "战士", "hp": 140, "mp": 26, "atk": 18, "def": 5,
          "skill": "盾击", "cost": 7,
          "desc": "生命与防御较高；盾击造成伤害，并打断敌人本回合的动作。"},
    "2": {"name": "法师", "hp": 105, "mp": 42, "atk": 16, "def": 3,
          "skill": "炎爆", "cost": 10,
          "desc": "炎爆造成高额伤害，穿透护甲；敌人的防御姿态仍能减伤。"},
    "3": {"name": "游侠", "hp": 120, "mp": 32, "atk": 17, "def": 4,
          "skill": "毒箭", "cost": 8,
          "desc": "普通攻击暴击率更高；毒箭附加三回合中毒，重复使用刷新持续时间。"},
}

GEAR = {
    "old_weapon": {"name": "旧武器", "slot": "weapon", "bonus": 0, "price": 0, "tier": 0},
    "old_armor": {"name": "旅行外衣", "slot": "armor", "bonus": 0, "price": 0, "tier": 0},
    "iron_weapon": {"name": "铁纹武器", "slot": "weapon", "bonus": 5, "price": 55, "tier": 1},
    "iron_armor": {"name": "铁纹护甲", "slot": "armor", "bonus": 3, "price": 45, "tier": 1},
    "silver_weapon": {"name": "银纹武器", "slot": "weapon", "bonus": 10, "price": 130, "tier": 2},
    "silver_armor": {"name": "银纹护甲", "slot": "armor", "bonus": 6, "price": 110, "tier": 2},
    "star_weapon": {"name": "星陨武器", "slot": "weapon", "bonus": 17, "price": 235, "tier": 3},
    "star_armor": {"name": "星陨护甲", "slot": "armor", "bonus": 10, "price": 200, "tier": 3},
}

ITEMS = {
    "potion": {"name": "生命药水", "price": 18, "amount": 65},
    "ether": {"name": "魔力药水", "price": 20, "amount": 28},
}

AREAS = [
    {"name": "回声森林", "boss": "荆棘守卫", "hp": 145, "atk": 19, "def": 4,
     "monsters": ["雾狼", "游荡树灵", "失路盗贼"],
     "rooms": ["battle", "treasure", "story", "battle"],
     "intro": "树梢挂着不会消散的白雾。第一枚封印碎片就在森林深处。"},
    {"name": "失落矿井", "boss": "噬晶巨像", "hp": 225, "atk": 29, "def": 7,
     "monsters": ["晶化矿工", "洞穴蛛", "岩穴守卫"],
     "rooms": ["battle", "trap", "story", "battle"],
     "intro": "废矿里传来有节奏的敲击声，像一颗仍在跳动的心脏。"},
    {"name": "无光高塔", "boss": "无光之王", "hp": 320, "atk": 38, "def": 10,
     "monsters": ["黑羽骑士", "空壳法师", "迷雾侍从"],
     "rooms": ["battle", "treasure", "story", "battle"],
     "intro": "天空没有星光。塔顶的王座上，有人在等待你的选择。"},
]


def ask(prompt, choices):
    """菜单只接受给定选项，输错不会消耗行动。"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices:
            return answer
        print("请输入这些选项之一：" + "、".join(choices))


@dataclass
class Player:
    name: str
    job: str
    max_hp: int
    hp: int
    max_mp: int
    mp: int
    base_atk: int
    base_def: int
    level: int = 1
    xp: int = 0
    gold: int = 45
    points: int = 0
    weapon: str = "old_weapon"
    armor: str = "old_armor"
    items: dict = field(default_factory=lambda: {"potion": 3, "ether": 2})
    equipment: list = field(default_factory=lambda: ["old_weapon", "old_armor"])

    @property
    def attack(self):
        return self.base_atk + GEAR[self.weapon]["bonus"]

    @property
    def defense(self):
        return self.base_def + GEAR[self.armor]["bonus"]

    @property
    def next_level(self):
        return 45 + (self.level - 1) * 25

    def recover(self, hp=0, mp=0):
        old_hp, old_mp = self.hp, self.mp
        self.hp = min(self.max_hp, self.hp + hp)
        self.mp = min(self.max_mp, self.mp + mp)
        return self.hp - old_hp, self.mp - old_mp


class Game:
    def __init__(self, player, save_path=SAVE_PATH, rng=None):
        self.p = player
        self.stage = 0
        self.room = 0
        self.rescued = False
        self.virtue = 0
        self.ending = ""
        self.save_path = Path(save_path)
        self.rng = rng if rng is not None else random.Random()

    def save(self, announce=True):
        """先写临时文件再替换，避免写到一半破坏旧存档。"""
        data = {
            "version": SAVE_VERSION, "player": asdict(self.p),
            "stage": self.stage, "room": self.room,
            "rescued": self.rescued, "virtue": self.virtue, "ending": self.ending,
        }
        temporary = self.save_path.with_suffix(".tmp")
        try:
            with temporary.open("w", encoding="utf-8") as handle:
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.flush()
                os.fsync(handle.fileno())
            temporary.replace(self.save_path)
        except OSError as error:
            print(f"存档失败：{error}。请把游戏放在允许写入的文件夹中。")
            return False
        if announce:
            print("进度已保存。")
        return True

    @classmethod
    def load(cls, save_path=SAVE_PATH):
        """只读取 JSON 数据，不执行存档中的任何代码。"""
        try:
            with Path(save_path).open(encoding="utf-8") as handle:
                data = json.load(handle)
            if not isinstance(data, dict) or data.get("version") != SAVE_VERSION:
                raise ValueError("存档版本不兼容")
            p = Player(**data["player"])
            cls.validate_player(p)
            game = cls(p, save_path)
            game.stage, game.room = data["stage"], data["room"]
            game.rescued, game.virtue = data["rescued"], data["virtue"]
            game.ending = data["ending"]
            if (type(game.stage) is not int or not 0 <= game.stage <= 3
                    or type(game.room) is not int or not 0 <= game.room <= 4
                    or type(game.rescued) is not bool
                    or type(game.virtue) is not int or not 0 <= game.virtue <= 3
                    or game.ending not in ("", "归途", "守夜人", "新王")):
                raise ValueError("冒险进度不合法")
            if game.stage == 3 and game.room != 0:
                raise ValueError("通关进度不合法")
            if game.ending and game.stage != 3:
                raise ValueError("结局与进度不一致")
            return game
        except FileNotFoundError:
            print("还没有存档，请先开始新冒险。")
        except (OSError, ValueError, TypeError, KeyError) as error:
            print(f"无法读取存档：{error}。原文件未被修改。")
        return None

    @staticmethod
    def validate_player(p):
        if not isinstance(p.name, str) or not 1 <= len(p.name) <= 16 or not p.name.isprintable():
            raise ValueError("角色名字不合法")
        if not isinstance(p.job, str) or p.job not in JOBS:
            raise ValueError("职业不合法")
        for key in ("max_hp", "hp", "max_mp", "mp", "base_atk", "base_def",
                    "level", "xp", "gold", "points"):
            value = getattr(p, key)
            if type(value) is not int or not 0 <= value <= 1_000_000:
                raise ValueError("角色数值不合法")
        if not (1 <= p.hp <= p.max_hp and 0 <= p.mp <= p.max_mp and p.level >= 1):
            raise ValueError("生命、魔力或等级不合法")
        if not isinstance(p.items, dict) or set(p.items) != set(ITEMS):
            raise ValueError("道具数据不合法")
        if any(type(n) is not int or not 0 <= n <= 10000 for n in p.items.values()):
            raise ValueError("道具数量不合法")
        if (not isinstance(p.equipment, list)
                or not all(isinstance(k, str) and k in GEAR for k in p.equipment)
                or len(p.equipment) != len(set(p.equipment))):
            raise ValueError("装备列表不合法")
        for slot in ("weapon", "armor"):
            key = getattr(p, slot)
            if not isinstance(key, str) or key not in p.equipment or GEAR[key]["slot"] != slot:
                raise ValueError("穿戴装备不合法")

    def gain_xp(self, amount):
        p = self.p
        p.xp += amount
        print(f"获得 {amount} 经验。")
        while p.xp >= p.next_level:
            p.xp -= p.next_level
            p.level += 1
            p.max_hp += 14
            p.max_mp += 3
            p.base_atk += 2
            p.base_def += 1
            p.points += 2
            p.recover(hp=30, mp=12)
            print(f"升级！当前 Lv.{p.level}，生命上限 +14，魔力上限 +3，攻击 +2，防御 +1。")
            print("获得 2 个属性点；回营地后可以自由分配。")

    def status(self):
        p = self.p
        print(f"\n{p.name} · {JOBS[p.job]['name']} · Lv.{p.level}")
        print(f"生命 {p.hp}/{p.max_hp}  魔力 {p.mp}/{p.max_mp}")
        print(f"攻击 {p.attack}  防御 {p.defense}  经验 {p.xp}/{p.next_level}")
        print(f"金币 {p.gold}  未分配属性点 {p.points}")
        print(f"武器：{GEAR[p.weapon]['name']}；护甲：{GEAR[p.armor]['name']}")
        job = JOBS[p.job]
        print(f"技能：{job['skill']}（{job['cost']} 魔力）。{job['desc']}")
        print("同伴：侦察员阿岚，每 4 个战斗回合治疗你 10 点生命。" if self.rescued else "同伴：暂无")

    def use_item(self):
        p = self.p
        print(f"1. 生命药水 ×{p.items['potion']}（恢复 65 HP）")
        print(f"2. 魔力药水 ×{p.items['ether']}（恢复 28 MP）  0. 返回")
        choice = ask("使用：", ("1", "2", "0"))
        if choice == "0":
            return False
        key = "potion" if choice == "1" else "ether"
        if p.items[key] <= 0:
            print("没有这种药水。")
            return False
        if (key == "potion" and p.hp == p.max_hp) or (key == "ether" and p.mp == p.max_mp):
            print("已经回满了，药水未消耗。")
            return False
        p.items[key] -= 1
        hp, mp = p.recover(hp=65 if key == "potion" else 0, mp=28 if key == "ether" else 0)
        print(f"使用{ITEMS[key]['name']}，恢复 {hp if key == 'potion' else mp} 点。")
        return True

    def backpack(self):
        while True:
            print("\n背包：1. 使用药水  2. 更换装备  0. 返回")
            choice = ask("选择：", ("1", "2", "0"))
            if choice == "0":
                return
            if choice == "1":
                self.use_item()
                continue
            mapping = {str(i): key for i, key in enumerate(self.p.equipment, 1)}
            for number, key in mapping.items():
                gear = GEAR[key]
                stat = "攻击" if gear["slot"] == "weapon" else "防御"
                worn = "（已穿戴）" if key in (self.p.weapon, self.p.armor) else ""
                print(f"{number}. {gear['name']}：{stat} +{gear['bonus']}{worn}")
            selection = ask("选择装备，0 返回：", tuple(mapping) + ("0",))
            if selection != "0":
                key = mapping[selection]
                setattr(self.p, GEAR[key]["slot"], key)
                print(f"已装备{GEAR[key]['name']}。")

    def merchant(self):
        p = self.p
        while True:
            print(f"\n流动商人 · 你有 {p.gold} 金币")
            print("1. 生命药水（18 金）  2. 魔力药水（20 金）")
            print("3. 购买装备  4. 出售闲置装备  0. 返回")
            choice = ask("选择：", ("1", "2", "3", "4", "0"))
            if choice == "0":
                return
            if choice in ("1", "2"):
                key = "potion" if choice == "1" else "ether"
                if p.gold < ITEMS[key]["price"]:
                    print("金币不足。")
                else:
                    p.gold -= ITEMS[key]["price"]
                    p.items[key] += 1
                    print(f"买到了{ITEMS[key]['name']}。")
                continue
            if choice == "3":
                keys = [k for k, g in GEAR.items()
                        if 0 < g["tier"] <= self.stage + 1 and k not in p.equipment]
            else:
                keys = [k for k in p.equipment if k not in (p.weapon, p.armor) and GEAR[k]["price"] > 0]
            if not keys:
                print("目前没有可交易的装备。出售前需要先换下装备。")
                continue
            mapping = {str(i): key for i, key in enumerate(keys, 1)}
            for number, key in mapping.items():
                gear = GEAR[key]
                price = gear["price"] if choice == "3" else gear["price"] // 2
                stat = "攻击" if gear["slot"] == "weapon" else "防御"
                print(f"{number}. {gear['name']}（{stat} +{gear['bonus']}）：{price} 金")
            selection = ask("选择编号，0 返回：", tuple(mapping) + ("0",))
            if selection == "0":
                continue
            key = mapping[selection]
            if choice == "4":
                p.equipment.remove(key)
                p.gold += GEAR[key]["price"] // 2
                print("出售成功。")
            elif p.gold < GEAR[key]["price"]:
                print("金币不足。")
            else:
                p.gold -= GEAR[key]["price"]
                p.equipment.append(key)
                setattr(p, GEAR[key]["slot"], key)
                print(f"买入并装备了{GEAR[key]['name']}。")

    def train(self):
        p = self.p
        while p.points > 0:
            print(f"\n剩余 {p.points} 点：1. 力量（攻击 +2） 2. 体质（生命上限 +12）")
            print("3. 专注（魔力上限 +6） 4. 坚韧（防御 +1） 0. 返回")
            choice = ask("加点：", ("1", "2", "3", "4", "0"))
            if choice == "0":
                return
            if choice == "1":
                p.base_atk += 2
            elif choice == "2":
                p.max_hp += 12
                p.hp += 12
            elif choice == "3":
                p.max_mp += 6
                p.mp += 6
            else:
                p.base_def += 1
            p.points -= 1
            print("属性已提升。")
        print("暂无可分配的属性点，升级后会获得新点数。")

    def rest(self):
        p = self.p
        if p.hp == p.max_hp and p.mp == p.max_mp:
            print("你现在状态很好，无需休息。")
            return
        cost = 10 + self.stage * 6 + p.level * 2
        print(f"旅店休息需要 {cost} 金币，恢复全部生命和魔力。")
        if p.gold < cost:
            print("金币不足。旅店老板允许你打工抵宿费，代价是花掉这一晚。")
            choice = ask("1. 打工后免费休息  0. 返回：", ("1", "0"))
            if choice == "1":
                p.recover(hp=p.max_hp, mp=p.max_mp)
                print("你搬完最后一捆柴火，在壁炉边睡了一晚。生命和魔力已回满。")
        elif ask("1. 付钱休息  0. 返回：", ("1", "0")) == "1":
            p.gold -= cost
            p.recover(hp=p.max_hp, mp=p.max_mp)
            print("一夜无梦，生命和魔力已回满。")

    def journal(self):
        print("\n目标：取得三枚封印碎片，登上无光高塔，决定迷雾的命运。")
        for index, area in enumerate(AREAS):
            state = "已取得碎片" if index < self.stage else "尚未解锁"
            if index == self.stage:
                state = f"探索 {self.room}/4，" + ("可以挑战守关者" if self.room == 4 else "正在推进")
            print(f"{index + 1}. {area['name']}：{state}")
        print("每个区域有四个探索地点和一个守关者；每次探索后返回营地补给。")
        print("深入岔道会遭遇更强敌人，并获得更多经验和金币。")
        print("失败或逃跑不推进地点；战败损失四分之一金币，然后恢复状态回营地。")
        print("地图、商店、背包中的选择不消耗战斗回合；战斗中喝药会消耗一回合。")

    def make_enemy(self, boss=False, elite=False):
        area, stage = AREAS[self.stage], self.stage
        if boss:
            return {"name": area["boss"], "hp": area["hp"], "max_hp": area["hp"],
                    "atk": area["atk"], "def": area["def"], "boss": True,
                    "xp": 70 + stage * 40, "gold": 75 + stage * 45}
        hp = 65 + stage * 30 + (20 if elite else 0)
        return {"name": ("精英·" if elite else "") + self.rng.choice(area["monsters"]),
                "hp": hp, "max_hp": hp, "atk": 12 + stage * 6 + (3 if elite else 0),
                "def": 2 + stage * 3, "boss": False,
                "xp": 26 + stage * 12 + (15 if elite else 0),
                "gold": 23 + stage * 13 + (18 if elite else 0)}

    def enemy_intent(self, enemy, turn):
        if enemy["boss"] and self.stage == 1 and turn % 4 == 0:
            return "heal"
        if turn % 3 == 0:
            return "heavy"
        if turn % 4 == 0:
            return "guard"
        return "attack"

    def battle(self, enemy):
        """每轮依次：持续伤害 → 展示意图 → 玩家行动 → 敌人行动。"""
        p = self.p
        turn, poison, enraged = 1, 0, False
        print(f"\n遭遇 {enemy['name']}！")
        while p.hp > 0 and enemy["hp"] > 0:
            if poison > 0:
                damage = 4 + p.level
                enemy["hp"] -= damage
                poison -= 1
                print(f"中毒发作：{enemy['name']}失去 {damage} HP。")
                if enemy["hp"] <= 0:
                    break
            if enemy["boss"] and self.stage == 2 and not enraged and enemy["hp"] <= enemy["max_hp"] // 2:
                enemy["atk"] += 6
                enraged = True
                print("无光之王进入狂暴阶段！攻击永久提升 6 点。")
            intent = self.enemy_intent(enemy, turn)
            labels = {"attack": "普通攻击", "heavy": "蓄力重击（伤害高，适合防御或打断）",
                      "guard": "防御（本轮受到伤害减半，不会攻击）",
                      "heal": "吸收晶体（本轮治疗自己，可以打断）"}
            print(f"\n第 {turn} 回合 | 你 HP {p.hp}/{p.max_hp} MP {p.mp}/{p.max_mp}")
            print(f"{enemy['name']} HP {max(0, enemy['hp'])}/{enemy['max_hp']} | 意图：{labels[intent]}")
            print(f"1. 攻击  2. {JOBS[p.job]['skill']}（{JOBS[p.job]['cost']} MP）")
            print("3. 防御（本轮受伤降为 40%，恢复 5 MP）  4. 药水  5. 敌人信息  6. 逃跑")
            defending, interrupted = False, False
            # 内层循环处理无效输入，防止它触发敌人攻击或额外中毒伤害。
            while True:
                action = ask("行动：", ("1", "2", "3", "4", "5", "6"))
                if action == "5":
                    print(f"敌人攻击 {enemy['atk']}、防御 {enemy['def']}。你先行动，重击约为普通攻击的 1.8 倍。")
                    print("守关者无法逃跑。盾击能打断行动；毒箭在后续三轮开始时生效。")
                    continue
                if action == "2" and p.mp < JOBS[p.job]["cost"]:
                    print("魔力不足，可以防御恢复魔力，或使用魔力药水。")
                    continue
                if action == "4" and not self.use_item():
                    continue
                if action == "6":
                    if enemy["boss"]:
                        print("封印关闭了退路，这场战斗无法逃跑！")
                        continue
                    if self.rng.random() < 0.65:
                        print("逃跑成功，回到营地；当前地点尚未完成。")
                        return "fled"
                    print("逃跑失败！敌人趁机行动。")
                break
            if action in ("1", "2"):
                raw = p.attack + self.rng.randint(-2, 3)
                armor = enemy["def"]
                if action == "1":
                    if self.rng.random() < (0.24 if p.job == "3" else 0.12):
                        raw = int(raw * 1.6)
                        print("暴击！")
                else:
                    p.mp -= JOBS[p.job]["cost"]
                    if p.job == "1":
                        raw = int(raw * 1.45)
                        interrupted = True
                    elif p.job == "2":
                        raw = int(raw * 2.0)
                        armor = 0
                    else:
                        raw = int(raw * 1.3)
                        poison = 3
                damage = max(1, raw - armor)
                if intent == "guard":
                    damage = max(1, damage // 2)
                enemy["hp"] -= damage
                print(f"你造成了 {damage} 点伤害。")
                if action == "2" and p.job == "3":
                    print("敌人中毒，将在后续三轮开始时受到伤害。")
            elif action == "3":
                defending = True
                _, recovered = p.recover(mp=5)
                print(f"你稳住阵脚，恢复 {recovered} MP。")
            if enemy["hp"] <= 0:
                break
            if interrupted:
                print("盾击打断了敌人的动作！")
            elif intent == "heal":
                amount = min(28, enemy["max_hp"] - enemy["hp"])
                enemy["hp"] += amount
                print(f"敌人吸收晶体，恢复 {amount} HP。")
            elif intent == "guard":
                print("敌人保持防御，没有发动攻击。")
            else:
                damage = max(1, int(enemy["atk"] * (1.8 if intent == "heavy" else 1))
                             + self.rng.randint(-2, 2) - p.defense)
                if defending:
                    damage = max(1, int(damage * 0.4))
                p.hp = max(0, p.hp - damage)
                print(f"{enemy['name']}造成 {damage} 点伤害。")
            if p.hp > 0 and self.rescued and turn % 4 == 0:
                recovered, _ = p.recover(hp=10)
                print(f"阿岚替你包扎，恢复 {recovered} HP。")
            turn += 1
        if p.hp <= 0:
            lost = p.gold // 4
            p.gold -= lost
            p.hp, p.mp = p.max_hp, p.max_mp
            print(f"\n你倒下了。救援队把你带回营地，遗失 {lost} 金币。生命与魔力已恢复。")
            print("当前地点尚未完成，装备、经验和之前的进度保留。")
            return "lost"
        p.gold += enemy["gold"]
        print(f"\n战斗胜利！获得 {enemy['gold']} 金币。")
        self.gain_xp(enemy["xp"])
        p.recover(mp=5)
        if self.rng.random() < 0.35:
            p.items["potion"] += 1
            print("战利品：生命药水 ×1。")
        return "won"

    def treasure(self):
        print("\n你找到商队留下的三只箱子，只能带走其中一箱。")
        print("1. 钱箱  2. 补给箱（生命药水 ×2，魔力药水 ×1）  3. 未鉴定装备箱")
        choice = ask("带走哪箱：", ("1", "2", "3"))
        if choice == "1":
            amount = 40 + self.stage * 25
            self.p.gold += amount
            print(f"获得 {amount} 金币。")
        elif choice == "2":
            self.p.items["potion"] += 2
            self.p.items["ether"] += 1
            print("补给已装进背包。")
        else:
            key = self.rng.choice([k for k, g in GEAR.items() if g["tier"] == self.stage + 1])
            if key in self.p.equipment:
                amount = GEAR[key]["price"] // 2
                self.p.gold += amount
                print(f"发现重复装备，换得 {amount} 金币。")
            else:
                self.p.equipment.append(key)
                print(f"获得{GEAR[key]['name']}！可在背包中装备。")

    def story(self):
        p = self.p
        if self.stage == 0:
            print("\n倒下的侦察员阿岚向你求救：‘我知道塔里的秘密……’")
            print("1. 给她一瓶生命药水  2. 花 20 金币雇人救她  3. 留下路标，独自离开")
            while True:
                choice = ask("你的选择：", ("1", "2", "3"))
                if choice == "1" and p.items["potion"] < 1:
                    print("你没有生命药水，请选择其他方式。")
                    continue
                if choice == "2" and p.gold < 20:
                    print("金币不足，请选择其他方式。")
                    continue
                break
            if choice != "3":
                if choice == "1":
                    p.items["potion"] -= 1
                else:
                    p.gold -= 20
                self.rescued = True
                self.virtue += 1
                print("阿岚加入队伍！此后每 4 个战斗回合为你恢复 10 HP。")
            else:
                print("你留下路标。雾重新吞没了她的身影。")
        elif self.stage == 1:
            print("\n矿井里的钟灵说：‘给我一点生命，我便告诉你封印的真相。’")
            print("1. 献出 18 HP（至少需要 19 HP，永久防御 +2）  2. 拿走祭坛上的 55 金币")
            while True:
                choice = ask("你的选择：", ("1", "2"))
                if choice == "1" and p.hp <= 18:
                    print("你的生命不足以承受仪式。")
                    continue
                break
            if choice == "1":
                p.hp -= 18
                p.base_def += 2
                self.virtue += 1
                print("钟灵赐予你防护，并透露：封印可以修复，但需要有人记得回家的路。")
            else:
                p.gold += 55
                print("你收下金币，钟声从此沉寂。")
        else:
            print("\n高塔脚下，难民守着最后一盏灯。他们请求你留下补给。")
            print("1. 捐出 35 金币（恢复 35 HP，获得 30 经验）  2. 接受他们赠送的药水和 25 金币")
            while True:
                choice = ask("你的选择：", ("1", "2"))
                if choice == "1" and p.gold < 35:
                    print("金币不足，请选择其他选项。")
                    continue
                break
            if choice == "1":
                p.gold -= 35
                self.virtue += 1
                p.recover(hp=35)
                self.gain_xp(30)
                print("他们替你处理伤口，并承诺让这盏灯一直亮着。")
            else:
                p.gold += 25
                p.items["potion"] += 1
                print("‘请一定终结这场迷雾。’老人把补给递给了你。")

    def trap(self):
        print("\n吊桥断了，桥底传来怪物的声音。")
        print("1. 沿岩壁攀爬（损失至多 14 HP，不致死，找到 25 金币）")
        print("2. 租绳索（18 金币，获得 12 经验）  3. 下去迎战精英敌人")
        while True:
            choice = ask("怎么过去：", ("1", "2", "3"))
            if choice == "2" and self.p.gold < 18:
                print("金币不足。")
                continue
            break
        if choice == "1":
            lost = min(14, self.p.hp - 1)
            self.p.hp -= lost
            self.p.gold += 25
            print(f"你擦伤了手臂，损失 {lost} HP，在岩缝里找到 25 金币。")
        elif choice == "2":
            self.p.gold -= 18
            self.gain_xp(12)
        else:
            return self.battle(self.make_enemy(elite=True)) == "won"
        return True

    def explore(self):
        area = AREAS[self.stage]
        print(f"\n{area['name']}：{area['intro']}")
        if self.room == 4:
            print(f"守关者 {area['boss']} 挡住了去路。这场战斗不能逃跑。")
            if ask("1. 挑战  0. 返回补给：", ("1", "0")) == "0":
                return
            if self.battle(self.make_enemy(boss=True)) == "won":
                self.stage += 1
                self.room = 0
                print(f"取得封印碎片！当前 {self.stage}/3。")
                self.p.recover(hp=self.p.max_hp, mp=self.p.max_mp)
                print("碎片的光芒让你的生命与魔力完全恢复。")
                if self.stage < 3:
                    print(f"新区域与商店装备已解锁：{AREAS[self.stage]['name']}。")
            return
        kind = area["rooms"][self.room]
        print(f"探索地点 {self.room + 1}/4")
        completed = True
        if kind == "battle":
            print("1. 沿主路前进  2. 深入岔道（精英敌人，更多奖励）  0. 返回")
            choice = ask("路线：", ("1", "2", "0"))
            if choice == "0":
                return
            completed = self.battle(self.make_enemy(elite=choice == "2")) == "won"
        elif kind == "treasure":
            self.treasure()
        elif kind == "story":
            self.story()
        elif kind == "trap":
            completed = self.trap()
        if completed:
            self.room += 1
            print(f"地点已完成，回到营地。当前进度 {self.room}/4。")

    def finale(self):
        if not self.ending:
            print("\n王座崩塌了。三枚碎片在你的手中重新拼成一枚钥匙。")
            print("1. 修复封印，让迷雾散去  2. 继承王座，掌握迷雾的力量")
            choice = ask("最终选择：", ("1", "2"))
            if choice == "2":
                self.ending = "新王"
            else:
                self.ending = "归途" if self.rescued and self.virtue >= 2 else "守夜人"
            self.save(announce=False)
        descriptions = {
            "归途": "阿岚拉住你的手，带你走出崩塌的高塔。灯火在远处亮起，你终于看见清晨。",
            "守夜人": "迷雾散去，你却留在封印另一侧。此后的每个黎明，都有人记得那位守夜人。",
            "新王": "你坐上王座，迷雾向你俯首。世界获得了暂时的安宁，也迎来了新的统治者。",
        }
        print(f"\n达成结局：《{self.ending}》")
        print(descriptions[self.ending])
        print(f"角色：{self.p.name} · {JOBS[self.p.job]['name']} · Lv.{self.p.level}")
        print("本次冒险结束。重新运行并选择新冒险，可以体验其他职业与结局。")

    def run(self):
        while self.stage < 3:
            p = self.p
            print(f"\n【篝火营地】{AREAS[self.stage]['name']} · 探索 {self.room}/4 · 碎片 {self.stage}/3")
            print(f"{p.name} Lv.{p.level} | HP {p.hp}/{p.max_hp} | MP {p.mp}/{p.max_mp} | 金币 {p.gold}")
            print("1. 探索 / 挑战守关者  2. 角色状态  3. 背包与装备")
            print("4. 商人  5. 旅店休息  6. 升级加点  7. 任务日志  8. 保存  0. 保存并退出")
            choice = ask("选择：", ("1", "2", "3", "4", "5", "6", "7", "8", "0"))
            if choice == "0":
                if self.save():
                    print("你把冒险记录收进背包。下次见！")
                    return
                if ask("存档失败。1. 留在游戏  2. 放弃未保存进度并退出：", ("1", "2")) == "2":
                    return
                continue
            actions = {"1": self.explore, "2": self.status, "3": self.backpack,
                       "4": self.merchant, "5": self.rest, "6": self.train,
                       "7": self.journal, "8": self.save}
            actions[choice]()
            if choice in ("1", "3", "4", "5", "6"):
                self.save(announce=False)
        self.finale()


def new_game(save_path=SAVE_PATH):
    print("\n雾灾已经持续七年。你来到边境营地，寻找失散在三处遗迹中的封印碎片。")
    name = input("给冒险者起个名字（直接回车使用‘旅人’）：").strip() or "旅人"
    name = "".join(ch for ch in name if ch.isprintable())[:16] or "旅人"
    for key, job in JOBS.items():
        print(f"{key}. {job['name']} | HP {job['hp']} MP {job['mp']} | {job['desc']}")
    choice = ask("选择职业：", ("1", "2", "3"))
    job = JOBS[choice]
    p = Player(name=name, job=choice, max_hp=job["hp"], hp=job["hp"],
               max_mp=job["mp"], mp=job["mp"], base_atk=job["atk"], base_def=job["def"])
    game = Game(p, save_path)
    game.save(announce=False)
    return game


def main():
    print("\n迷 雾 地 牢")
    print("探索 · 回合制战斗 · 三种职业 · 装备成长 · 多结局")
    print("所有操作：输入菜单数字，然后按 Enter。")
    while True:
        print("\n1. 新冒险  2. 读取存档  3. 玩法说明  0. 退出")
        choice = ask("选择：", ("1", "2", "3", "0"))
        if choice == "0":
            return
        if choice == "3":
            print("三大区域各有四个地点和一名守关者。探索、整备、挑战，收集全部碎片。")
            print("看清敌人意图再行动：蓄力重击时可以防御，战士还能用盾击打断。")
            print("战败会损失四分之一金币并回营地；没有永久死亡，可以继续尝试。")
            print("每次行动返回营地后自动存档，营地选 0 保存退出。战斗中无法存档。")
            print("背包、商店、加点的变更在返回营地后保存。Ctrl+C 中断会丢失最近保存后的变更。")
            print("只有一个存档槽：mist_dungeon_save.json，位于游戏脚本所在文件夹。")
            continue
        if choice == "1":
            if SAVE_PATH.exists() and ask("新冒险将覆盖现有存档。1. 确认  0. 返回：", ("1", "0")) == "0":
                continue
            game = new_game()
        else:
            game = Game.load()
        if game is not None:
            game.run()
            return


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n游戏已中断。下次可读取最近一次成功保存的进度。")
