"""猜数字小游戏：用 Python 3 运行，无需安装第三方库。

启动命令：python guess_number.py
"""

import random


def play_round():
    """玩一局；正常结束返回 True，主动退出返回 False。"""
    # randint(1, 100) 会随机选出一个 1～100 的整数，包含两端。
    answer = random.randint(1, 100)
    chances = 7
    used = 0

    print("\n我想好了一个 1～100 的整数，你有 7 次机会！")
    print("我会提示偏大或偏小。输入 q 可以退出。")

    while used < chances:
        text = input(f"\n剩余 {chances - used} 次机会，你猜：").strip()

        if text.lower() == "q":
            return False

        # input() 得到的是字符串，需要转换成整数才能比较大小。
        try:
            guess = int(text)
        except ValueError:
            print("请输入整数，例如 50。这次不扣机会。")
            continue

        if guess < 1 or guess > 100:
            print("数字要在 1～100 之间。这次不扣机会。")
            continue

        used += 1

        if guess == answer:
            print(f"恭喜猜中！答案就是 {answer}，你用了 {used} 次。")
            return True
        elif guess < answer:
            print("猜小了，试试更大的数字！")
        else:
            print("猜大了，试试更小的数字！")

    print(f"机会用完了！正确答案是 {answer}。")
    return True


def main():
    print("=== 猜数字小游戏 ===")

    while play_round():
        again = input("\n再玩一局？输入 y 继续，其他内容退出：").strip()
        if again.lower() != "y":
            break

    print("游戏结束，下次再来！")


# 直接运行这个文件时，才启动游戏。
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\n游戏结束，下次再来！")
