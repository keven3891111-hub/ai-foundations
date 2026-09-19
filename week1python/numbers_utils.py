#自然数加和
def sum_to_n(n):
    total = 0
    number =1

    while number <= n:
        total += number
        number +=1

    return total
#增加非负元素直到0为止
def collect_until_zero (values):
    result = []
    for value in values:
        if value < 0:
            continue
        elif value == 0:
            break
        else:
            result.append(value)

    return result
#把字符串转换为整数列表
def parse_numbers(text):
    cleaned = text.strip()
    parts = cleaned.split(",")

    numbers = [
        int(part)
        for part in parts
    ]

    return numbers
#对输入的整数进行错误处理
def read_positive_integer():
    while True:
        try:
            n = int(input("请输入正整数："))

            if n > 0:
                return n
            else:
                print("数字必须大于0")
        except ValueError:
            print("格式错误，请输入整数")
#输入数字以及检查格式错误
def read_numbers():
    while True:
        text = input("请输入逗号间隔的整数:")

        try:
            numbers = parse_numbers(text)
            break

            # print(numbers)
        except ValueError:
            print("格式错误")
    return numbers

def read_history(filename):
    try:
        with open(filename, "r", encoding="utf=8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        with open(filename, "w", encoding="utf=8") as file:
            pass
        return ""

def save_history(filename, text):
    #以追加模式打开filename,使用utf-8
    #写入text,并在末尾添加一个换行符
    with open(filename, "a", encoding="utf=8") as file:
        file.write(text + "\n")

def find_first_positive(values):
    for value in values:
        if value > 0:
            return value
    return None





















