import json

# case = {
#     "values": [2, -1, 0, 1],
#     "limit": -2,
#     "expected": [2, -1]
# }

# 1. 将字典保存到文件
# with open("case.json", "w", encoding="utf-8") as file:
#     json.dump(case, file, indent=4)
#
# # 2. 从文件读取数据
# with open("case.json", "r", encoding="utf-8") as file:
#     restored = json.load(file)
#
# # 3. 检查读取的结果
# print(restored["values"])
# print(restored == case)
# print(restored["limit"] == 5)

import json

# with open("case.json", "r", encoding="utf-8") as file:
#     restored = json.load(file)
#
# print(restored["limit"])

import json

def save_json(data, filename):
    # 将 data 保存到 filename 指定的文件
    # 你来完成
    with open(filename, 'w',encoding = "utf-8") as file:
        json.dump(data, file,indent=4)

# save_json({"values": [3, 8], "limit": 5},
#           "practice_data.json")

def load_records(filename):
    """读取并返回记录列表；文件不存在时返回 []。"""
    # 你来完成
    try:
        # 尝试执行可能报错的代码
        with open(filename, "r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        # 文件不存在时，执行这里
        records = []
    return records
# 准备一个确实存在的文件
# save_json(
#     [{"subject": "Python", "minutes": 30}],
#     "read_check.json"
# )
#
# # 检查正常读取
# records = load_records("read_check.json")
# print("已有文件：", records)
#
# # 检查文件不存在的情况：请确保这个文件名尚未创建
# empty_records = load_records("missing_records_check.json")

# def add_record(filename,subject,minutes):
#     if minutes <= 0:
#         return False
#     records = load_records(filename)
#
#     records.append({"subject": subject, "minutes": minutes})
#     save_json(records, filename)
#     return True
# # 准备测试：文件里已经有一条旧记录
# save_json(
#     [{"subject": "Python", "minutes": 30}],
#     "add_check.json"
# )
#
# print(add_record("add_check.json", "JSON", 20))
# print(add_record("add_check.json", "Python", -5))
# print(load_records("add_check.json"))

# records = [
#     {"subject": "Python", "minutes": 30},
#     {"subject": "JSON", "minutes": 20},
#     {"subject": "Python", "minutes": 45},
#     {"subject": "math", "minutes": 15}
# ]
# # records = {"subject": "Python", "minutes": 30}
#
#
# def summarize_minutes(records):
#     # 返回“科目 → 累计分钟数”的字典
#     # 你来完成
#     totals = {}
#     for record in records:
#         subject = record["subject"]
#         minutes = record["minutes"]
#
#         previous = totals.get(subject,0)  # 取出这个科目之前的总时长
#         print(previous, minutes)
#         totals[subject] = previous + minutes  # ② 加上本次时长，存回字典
#
#     return totals

# print(summarize_minutes(records))



# def summarize_minutes(records):
#     totals = {}                       # ① 用字典保存各科目的总时长
#
#     for record in records:
#         subject = record["subject"]
#         minutes = record["minutes"]
#
#         previous = totals.get(subject, 0)   # 取出这个科目之前的总时长
#         totals[subject] = previous + minutes  # ② 加上本次时长，存回字典
#
#     return totals                     # ③ 全部统计完成后，返回字典
#
#
# print(summarize_minutes(records))

records = [
    {"subject":"Python","minutes":30},
    {"subject":"JSON","minutes":20},
    {"subject": "Python", "minutes": 45},
    {"subject": "math", "minutes": 20},
]
#
# def summarize_minutes(records):
#     total = {}
#     for record in records:
#         subject = record["subject"]
#         minutes = record["minutes"]
#         previous = total.get(subject,0)
#         total[subject] = previous+ minutes
#
#     return total
# print(summarize_minutes(records))

def find_records(records, target_subject):
    result = []

    for record in records:
        if record["subject"]==target_subject:                 # ① 当前记录的科目是否等于目标科目？
            result.append(record)  # ② 把当前这整个字典加入结果列表

    return result


print(find_records(records, "Python"))
print(find_records(records, "英语"))






















