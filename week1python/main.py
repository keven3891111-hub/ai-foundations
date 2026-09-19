# def demo():
#     for n in [1, 2, 3]:
#         if n == 2:
#             return n
#
#         print(n)
#
#     print("循环之后")
#     return 99
#
#
# result = demo()
# print("接收到：", result)
from enum import nonmember


# from numbers_utils import*
# print(find_first_positive([-2, 0, 5, 8]))
# print(find_first_positive([-3, 0, -1]))

# def find_first_positive(values,limit):
#     for value in values:
#         if value > limit:
#             return value
#
#
# result = find_first_positive([1, 4, 7, 9],5)
# print("最终结果",result)


def collect_above(values, limit):
    text = []
    for value in values:
        if value == 0:
            break
        elif value > limit:
            text.append(value)
    return text
#
# assert collect_above([2, -1, 0, 1], -2) == [2,-1]
#
#

# print("检查完成")
# case = {
#     "values": [2,-1,0,1],
#     "limit": -2,
#     "expected": [2,-1]
# }
# actual = collect_above(case["values"], case["limit"])
# assert actual== case["expected"]
#
#
# print("检查完成")

cases = [
    {"values": [2, 7, 0, 9], "limit": 5, "expected": [7]},
    {"values": [2, -1, 0, 1], "limit": -2, "expected": [2,-1]},
    {"values": [], "limit": 5, "expected": []},
    {"values": [5,6,0,8], "limit": 5, "expected": [6]}
]

for case in cases:
    actual = collect_above(case["values"], case["limit"])
    assert actual == case["expected"], (f"预期：{case['expected']}，"
                                        f"实际：{actual}")

print("全部检查通过")





















