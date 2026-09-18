# from numbers_utils import sum_to_n
#
# n = 7
# total = sum_to_n(n)
#
# with open('result.txt', "a",encoding="utf=8") as file:
#     file.write(f"1到{n}的和为：{total}\n")
#
# print("保存完成")

# from numbers_utils import sum_to_n

# n = 7
# total = sum_to_n(n)
def read_history(filename):
    try:
        with open(filename, "r", encoding="utf=8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        with open(filename, "w", encoding="utf=8") as file:
            pass
        return ""


text = read_history("result.txt")
if text == "":
    print("暂无历史记录")
else:
    print(text)


# print(type(content))