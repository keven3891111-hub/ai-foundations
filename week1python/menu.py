"""
# 周日代码
# name = "keven"
# age = 24
# print("你好",name)
# print("明年",age+1)

scores = [90, 95, 89]
# print(scores)

average = sum(scores)/len(scores)
print("平均分",average)

if average >= 90:
    print("表现不错")
else:
    print("继续努力")

name = "keven"
age = 22
height = 1.77
is_student = True
print(name,age,height,is_student)

age = 22
next_age = age + 1
print("当年年龄",age)
print("明年年龄",next_age)
print(type(age))
print(type(next_age))
print(type(height))

a = 5
b = "5"
print(a+5)
print(type(b+"5"))

age = 25
message ="我的年龄是"+str(age)
print(type(message))

a = int("3")+int("4")
b = str(3+4)
print(a,type(a))
print(b,type(b))

print(8/2)
print(8//2)
print(8/3)
print(8//3)

print(-7//2)
# ppppppppppppppppppppppppppppppp

print(7%2)
print(8%2)
print(2+3*4)
print((3+4)*4)
print(2**5)
score = 95
result = score>=90
print(result)
print(type(result))

score = 95
if score>90:
  print("优秀")
else:
  print("不优秀")
print("判断结束")

score = 90
if score>85:
  print("优秀")
elif score>=60:
  print("及格")
else: print("不及格")

number = -4
if number > 0 and number%2==0:
  print("正偶数")
else:
  print("不符合")

  numbers = [-2, 7, 0, 8]
  count = 0
  total = 0
  for x in numbers:

      if x > 0 and x % 2 == 0:
          count = count + 1
          total = total + x
          print("正偶数")
      else:
          print("不符合")
  if count > 0:
      print("正偶数平均值:", total / count)
  else:
      print("没有正偶数")
def add(a,b):
 return a + b
result = add(3,4)
print(result)

def is_positive_even(a):
 if a>0 and a%2==0:
  return True
 else:
  return False
print(is_positive_even(12))  # True
print(is_positive_even(9))   # False
print(is_positive_even(-4))  # False
print(is_positive_even(0))   # False

def count_positive_even(numbers):
  count = 0
  for a in numbers:
   if is_positive_even(a):
    count+=1

  return count

print(count_positive_even([6, -2, 7, 10, 0, 8]))  # 3
print(count_positive_even([-2, 7, 0]))             # 0
print(count_positive_even([]))                     # 0，空列表

def get_positive_evens(numbers):
  result = []
  for a in numbers:
   if is_positive_even(a):
    result.append(a)

  return result
print(get_positive_evens([6, -2, 7, 10, 0, 8]))
print(get_positive_evens([-2, 7, 0]))
print(get_positive_evens([]))

values = [1,2,3,4,5]
print(values[-1])

values = [1,2,3,4,5,6]
print(values[1:4])

numbers = [6,10,8,4,12]
print(numbers[:2])
print(numbers[2:])

for i in range(1,6):
 print(i)


 def sum_squares(n):
     total = 0
     for i in range(n + 1):
         total = total + i ** 2
     return total


 print(sum_squares(3))  # 14
 print(sum_squares(5))  # 55
 print(sum_squares(0))  #


 def product_to_n(n):
     total = 1
     for i in range(n):
         total = total * (i + 1)
     return total


 print(product_to_n(3))  # 6
 print(product_to_n(5))  # 120
experiment = {

  "name" : "baseline",
  "epoches" : 3,
  "learning rate" : 0.001
}
print(experiment["epoches"])
experiment["epoches"] = 5
print(experiment["epoches"])
experiment["epochs"] = 4
for i in range(experiment["epochs"]):
  a = i+1
  print("第",a,"轮")
logs =[
    {"epochs":1,"loss":0.8},
    {"epochs":2,"loss":0.6},
    {"epochs":3,"loss":0.2}

        ]
first_record = logs[0]
print(first_record)
first_loss = first_record["loss"]
print(first_loss)
print(logs[0]["loss"])


for record in logs:
  if record["loss"]<0.5:
  #print("第",record["epochs"],"轮,","loss:",record["loss"])
   print("第",record["epochs"],"轮，","loss:",record["loss"])

def filter_logs(logs, threshold):
  result = []
  for record in logs:
    if record["loss"]<threshold:
      result.append(record)
  return result
print(filter_logs(logs, 0.5))

print(filter_logs(logs, 0.1))

values = [1,2,3]
print(len(values))
print(len([]))

selected = filter_logs(logs,0.7)
print(len(selected))

selected = [
    {"epochs": 2, "loss": 0.6},
    {"epochs": 3, "loss": 0.2}
]
def average_loss(records):
  count = 0
  total_loss = 0
  for record in records:
    count = count + 1
    total_loss = total_loss + record["loss"]
  if count==0:
   return None
  return total_loss/count
print(average_loss(selected))  # 0.4
print(average_loss([]))        # None
print("hello")

def multiply(x, factor=2):
  return x*factor
multiply(3,4)
multiply(x=3,factor=4)
multiply(factor=4,x=3)

def calculate(a,b):
 return a+b,a*b
print(calculate(3,4))

values = [6,8,10]
for index,value in enumerate(values,start=1):
  print(index,value)

logs = [
    {"epochs": 2, "loss": 0.6},
    {"epochs": 5, "loss": 0.2},
    {"epochs": 9, "loss": 0.1}
]
for index, record in enumerate(logs, start=1):
  if record["loss"]<0.5:
   print(index,record["epochs"],record["loss"])

epochs = [2, 5, 9]
losses = [0.6, 0.2, 0.1]
logs = []
for epoch,loss in zip(epochs,losses):
#{2,0.6}l
 logs.append({"epoch":epoch,"loss":loss})
print(logs)
print(type(logs))
print(type(logs[0]))
print(type(logs[0]["loss"]))

loss_values = []

for record in logs:
    loss_values.append(record["epoch"])

print(loss_values)  # [0.6, 0.2, 0.1]

epoch_values = [
    record["epoch"]*2       # 每轮收集什么
    for record in logs   # 从哪里逐条取数据
]
print(epoch_values)

selected_epochs = [
    record["epoch"]*2
    for record in logs
     if record["loss"] < 0.5

]

print(selected_epochs)

loss_by_epoch = {
    record["epoch"]: record["loss"]
    for record in logs
    if record["loss"]<0.5
}

print(loss_by_epoch)
# {2: 0.6, 5: 0.2, 9: 0.1}

for epoch, loss in loss_by_epoch.items():
    print(epoch, loss)

config = {
    "epochs": 5,
    "batch_size": 4
}
for epoch, loss in config.items():
  print("参数",epoch,"的值是",loss)

name = "keven"
age = 25
message = f"{name}今年{age}岁"
print(message)

epoch = 5
loss = 0.1
print(f"第{epoch}轮的损失为{loss}")

epoch = 5
loss = 0.123456
logs = [
    {"epoch": 2, "loss": 0.63456},
    {"epoch": 5, "loss": 0.23456},
    {"epoch": 9, "loss": 0.12345}
]
for record in logs:
  if record["loss"]<0.5:
    print(f"第{record['epoch']}轮的损失为{record['loss']:.2f}")

record = {"epochs":1,"loss":0.2345}
print(record.get("loss", "未记录"))              # 0.23456
print(record.get("accuracy"))          # None
print(record.get("accuracy", "未记录"))  # 未记录

record = {"epochs":1,"loss":0.143}
record["loss"] = 0.05
record["accuracy"] = 0.98
print(record)

config = {"epochs": 5, "batch_size": 4}
config["epochs"] = 10
config["learning_rate"] = 0.001
if "seed" not in config:
    config["seed"] = 42
print(config)
print("epochs" in config)
print("seed" in config)
print("seed" not in config)

logs = [
    {"epoch": 2, "loss": 0.63456},
    {"epoch": 5, "loss": 0.23456},
    {"epoch": 9, "loss": 0.12345}
]
for index, record in enumerate(logs, start=1):
  if record["loss"]<0.5:
   print(f"记录{index},第{record['epoch']}轮，loss={record['loss']:.2f}")

data = {"a": 3, "b": 7}
result = {

    key: value + 1
    for key, value in data.items()
    if value >5
}
print(result)

data = {"a": 3, "b": 7}
result = {}

for key, value in data.items():
    if value > 5:
        result[key] = value + 1

print(result)

data = { "a":2, "b":6, "c":8  }
result={}
for key,value in data.items():
  if value>5:
    result[key] = value + 1
print(result)

def collect_even(values):
  result = []
  for i in values:
    if i%2 == 0:
      result.append(i)
  return result
print(collect_even([1, 4, 6]))  # 应输出 [4, 6]
print(collect_even([1, 3]))     # 应输出 []
print(collect_even([]))        # 应输出 []

student = {"name": "keven", "age": 25}
sdudent["age"] = 26
print(sdudent["age"])

print("hello world")
for value in [2, 8, 10]:
    print(value)

    if value > 5:
        break

print("循环结束")

print("hello")

print(f"第{epoch}轮的损失为{loss:.2f}")

9月16
日代码 周一 周二 周三
def collect_even(values):
  result = []
  for i in values:
    if i%2 == 0:
      result.append(i)
  return result
print(collect_even([1, 4, 6]))  # 应输出 [4, 6]
print(collect_even([1, 3]))     # 应输出 []
print(collect_even([]))        # 应输出 []



def update_age(age):
    student["age"] = 26


student = {"name": "keven", "age": 25}

A = student.copy()
update_age(A)

print(student)
print(A)

print("jason hello")

def double(x):
    anwswer =  x * 2
    return "修改完成"
value = double(3)
print(value)


def make_new(person):
    person = {"name": "keven", "age": 30}
    return person

student = {"name": "keven", "age": 25}

result = make_new(student)

print(student)
print(result)

def with_age(person, new_age=26):
    updated = person.copy()
    updated["age"] = new_age
    return updated


student = {"name": "keven", "age": 25}

result1 = with_age(student, 30)
result2 = with_age(student)

print(student)
print(result1)
print(result2)
def add(a, b):
    total = a + b
    return total

add(3, 4)
total = add(3, 4)
print(total)
for value in [2,6,8,11]:
    print(value)
    if value > 5:
        break
print("打印完成")

def collect_until_zero(values):
    result = []
    for value in values:
        if value < 0:
            continue
        if value ==0:
            break
        result.append(value)
    return result
print(collect_until_zero([2, -1, 4, 0, 8]))  # 应输出 [2, 4]
print(collect_until_zero([-1, 0, 5]))         # 应输出 []            # 应输出 []

count = 1
total = 0
while count <= 5:
    total = total + count
    count = count + 1
print(total)


name = input("请输入你的名字：")
print(f"你好，{name}")

num = int(input("请输入数字"))
n=0
total = 0
while n < num:
    n = n + 1
    total = total + n

print(total)
print(n)

data = {"a": 3, "b": 6, "c": 9}
result = {}
for key, value in data.items():
     if value > 5:
         result[key] = value * 2
print(result)

result = {
    key:value*2
    for key,value in data.items()
    if value > 5
}
print(result)

data = {"a": 3, "b": 6, "c": 9}
result = {
    key:value+1
    for key,value in data.items()
    if value>5
}
print(result)

def read_seed(config):
    value=config.get("seed",42)
    return value

config = {"epochs": 5}

value = read_seed(config)
print(value)   # 应输出 42
print(config)  # 应输出 {'epochs': 5}




n = int(input("请输入数字"))
i=1
total=0
while i < n+1:
    if i % 2 == 0:
     total = total + i
    i = i + 1
print(f"1到{n}的偶数和为{total}")
列表推导式的作用是：遍历数据，把每轮得到的结果收集成一个新列表。
要求：把字符串列表转换成整数列表
parts = ["2", "5", "8"]
numbers = []
常规解法  for循环
for part in parts:
    numbers.append(int(part))
print(numbers)

列表推导式
numbers = [
    int(a)
    for a in parts
]
print(numbers)
"""
from ctypes.wintypes import tagPOINT
from functools import partial
from turtledemo.penrose import start
from unittest import result


#
# text = " 2,5,8 "
# cleaned  = text.strip()
#
# parts = cleaned.split(",")
#
# numbers = [
#     int(part)
#     for part in parts
# ]
# print(numbers)
#
# try:
#     number =int (input("请输入整数"))
#     print(number*2)
# except ValueError:
#     print("输入格式错误")
#
# print("本次处理结束")

# while True:
#     try:
#         number = int(input("请输入正整数："))
#
#         if number > 0:
#             break
#         else:
#             print("数字必须大于0")
#
#     except ValueError:
#         print("输入格式错误，请输入整数")
#
# print(f"最终读到：{number}")
# def value():
#   while True:
#     try:
#         number = int(input("请输入整数："))
#         if number > 0:
#            return number
#         else:
#             print("数字必须大于0")
#     except ValueError:
#         print("输入格式错误，请输入整数")
#
# n=value()
#
# print(f"收到的整数是：{n}")

# def value():
#     while True:
#         try:
#             number = int(input("请输入整数："))
#             if number > 0:
#                 return number
#             else:
#                 print("数字必须大于0")
#         except ValueError:
#             print("输入格式错误，请输入整数")
#
# def sum_to_n(n):
#     total = 0
#     number = 0
#     while number < n:
#         number = number + 1
#         total = total + number
#     return total
# n = value()
# total = sum_to_n(n)
# print(f"1到{n}的和为：{total}")

# def parse_numbers(text):
#     text = text.strip()
#     text = text.split(",")
#     text = [
#         int(part)
#         for part in text
#     ]
#     return text
# print(parse_numbers("  2,-1,4,0,8  "))
#------------------------------2026.09.17------------
# def parse_number(text):
#     text = text.strip()
#     text = text.split(",")
#     text = [
#         int(part)
#         for part in text
#     ]
#     return text
# print(parse_number(" 2,3,-1,4 "))

#9月17日
#
# #类型 运算 与 切片
# text = "9"
# print(int(text)+3) #12
# print(9//2,9%2)    #4 1
# print(2*3,2**3)    #6,8
#
# values = [2,5,8,11]
# print(values[1:3]) #输出列表的第二到第三个元素 和 Range一样 不包括最后的元素
# print(values[-1]) #输出列表的最后一个元素
# """"
# ①
# 12
# 4,1
# 6,8
# [5,8]
# 11
# """
# # 字典取值与默认值
# config ={"epochs": 5}
# key = "epochs"
#
# print(config[key])
# print(config.get("seed", 42))
# print("seed" in config)
# print(config)
#
# """"
# ②
# 5
# 42
# False
# [5,8]
# {"epochs": 5}
# 并不会给字典添加seed，get是判断取值，没有就输出默认值 添加的命令是append
# """
# #修改列表与函数返回值
# def add_number (values):
#     values.append(9)
#
# numbers = [1,2]
# result = add_number(numbers)
#
# print(numbers)
# print(result)
# """"
# ③
# [1,2]
# [1,2,9]
# 因为result指向的是新的列表 ，是value指向的列表 不是numers列表本身
# """
# #字符串处理 与 列表推导式
# text = "2,-1,4,0,8"
# parts = text.strip().split(",")
#
# numbers=[
#     int(part)
#     for part in parts
# ]
# print(numbers)

# def add_number(values):
#     values.append(9)
#     return values
#
# numbers = [1,2]
# result = add_number(numbers)
#
# print(numbers)
# print(result)
#
# [1,2,9]
# [1,2,9]
# 指向同一份列表

#默认参数与解包
# def calculate(a,b=2):
#     return a + b, a*b
# x,y=calculate(3,b=4)
# print(x,y)
# print(calculate(3))

#复制与修改
# def update_config(config):
#     updated = config.copy()
#     updated["epochs"] = 10
#     return updated
# config = {"epochs":5}
# result = update_config(config)
# result["seed"] = 42
#
# print(config)
# print(result)
#
# {"epochs":5}
# {'epochs': 10, 'seed': 42}

#zip  编号 与 筛选
# epochs = [2,5,9]
# losses = [0.63456,0.23456]
#
# for index , (epoch, loss) in enumerate(zip(epochs, losses),start=1):
#     if loss < 0.5:
#         print(f"记录{index}:第{epoch}轮,loss={loss:.2f}")
#
# 两轮，最终打印
# 记录2：第5轮，loss=0.23
#独立写推导式 保留大于5的项目 并且值乘以2

# data = {"a": 3, "b": 6, "c": 9}
#
# result = [
#     value * 2
#     for value in data.values()
#     if value > 5
# ]
# # 输出: [3, 12, 18]
# print(result)

# result = {
#
#     key:value * 2
#     for key,value in data.items()
#     if value > 5
# }
# # 输出: [3, 12, 18]
# print(result)
#
# ⑨
# [2,4]
# 3
# ⑩
# [3,5]
# 8不会被处理，在输入0时 判断退出循环
# ⑪
# 开始
# 转换失败
# 结束
# ⑫

# def parse_numbers(text):
#     text = text.strip()
#     text = text.split(",")
#     result = [
#         int(part)
#         for part in text
#     ]
#     return result
# def read_numbers():
#     while True:
#         try:
#
# print(parse_numbers(" 3,-2,5,0,8 "))
# 预期：[3, -2, 5, 0, 8]

#示例
#1、把字符串转换为整数列表
# def parse_numbers(text):
#     text = text.strip()
#     parts = text.split(",")
#
#     result = [
#         int(part)
#         for part in parts
#     ]
#     return result
#
# #2、负责：读取输入，失败时重新询问
# def read_numbers():
#     while True:
#         text = input("请输入逗号分隔的整数：")
#
#         try :
#             numbers = parse_numbers(text)
#             return numbers
#         except ValueError:
#             print("格式错误，请确保每一项都是整数")
#
# #调用函数 输出结果
# numbers = read_numbers()
# print(f"读取结果：{numbers}")
#
# text = input("请输入逗号分隔的整数：")
# numbers = parse_numbers(text)
# try:
#     numbers = parse_numbers(text)
#     print(numbers)
# except ValueError:
#     print("格式错误，请重新输入")
# print(numbers)
# print(text)
# print("hello world")

# def parse_numbers(text):
#     text = text.strip()
#     text = text.split(",")
#     result = [
#         int(part)
#         for part in text
#     ]
#     return result
#
# def read_numbers():
#     while True:
#         text = input("请输入逗号分隔的整数：")
#
#         try:
#             numbers = parse_numbers(text)
#             return numbers
#         except ValueError:
#             print("格式错误，请重新输入")

#
# answer = read_numbers()
# print(f"读取结果：{answer}")

# def collect_until_zero(values):
#     result = []
#     for  i in  values:
#
#         if i < 0:
#            continue
#         elif i == 0:
#             break
#         # print(i)
#         else:
#             result.append(i)
#
#     return result
# print(collect_until_zero([2, -1, 4, 0, 8]))
# 预期：[2, 4]

#--------------------------------9.18-----------------------------------
# def add_number(values):
#     values.append(5)
#     return len(values)
#
# numbers = [1,3]
# result  = add_number(numbers)
#
# print(numbers)
# print(result)
# [1,3,5]
# 3

# data = {"a": 2, "b": 5, "c": 8}
# result = {
#     key:value*2
#     for key, value in data.items()
#     if value>3
# }
# print(result)

# {"b": 10, "c": 16}

#用户输入 2,-1,4,0,8，程序跳过负数，遇到 0 停止，最后得到 [2, 4]。
# 如果输入里有 abc 这样的内容，就提示重新输入。
# 字符串转换为 整数列表



# def parse_numbers(text):
#     cleaned = text.strip()
#     parts = cleaned.split(",")
#
#     numbers = [
#         int(part)
#         for part in parts
#     ]
#
#     return numbers
# #输入数字以及检查格式错误
# def read_numbers():
#     while True:
#         text = input("请输入逗号间隔的整数:")
#
#         try:
#             numbers = parse_numbers(text)
#             return numbers
#
#         except ValueError:
#             print("格式错误")
# 排除负数 遇到0停止
# def collect_until_zero (values):
#     result = []
#     for value in values:
#         if value < 0:
#             continue
#         elif value == 0:
#             break
#         else:
#             result.append(value)
#
#     return result

# def sum_to_n(n):
#     total = 0
#     number = 1
#
#     while number <=n:
#         total = total + number
#         number = number + 1
#     return total

# def read_positive_integer():
#     while True:
#         try:
#             n = int(input("请输入正整数："))
#
#             if n > 0:
#                 return n
#             else:
#                 print("数字必须大于0")
#         except ValueError:
#             print("格式错误，请输入整数")

from numbers_utils import *
#输入菜单 可选择功能
def main():
    while True:
        print("\n =====数字工具====")
        print("1:计算从1到n的和")
        print("2:处理整数列表")
        print("3：查看使用说明")
        print("4：查看历史记录")
        print("0:退出")
        # 等待用户选择功能
        choice = input("请选择功能")
        if choice == "1":
            n = read_positive_integer()
            total = sum_to_n(n)
            print(f"1到{n}的和为：{total}")
            save_history("result.txt", f"1到{n}的和为：{total}")
        elif choice == "2":
            # 调用已有函数 完成一次列表处理
            values = read_numbers()
            result = collect_until_zero(values)
            if result == []:
                print("没有收集到正整数，不保存此次记录")
            else:
                message = f"原始记录：{values},处理结果：{result}"
                print(message)
                save_history("result.txt", message)


        elif choice == "3":
            print("列表中的整数请使用英文逗号分隔。\n"
                  "处理列表时，跳过负数，遇到0停止")
        elif choice == "4":
           text = read_history("result.txt")
           if text == "":
               print("暂无历史记录")
           else:
               print(text)
        elif choice == "0":
            print("程序结束")
            break
        else:
            print("无效选项，请重新选择")
# main()
if __name__=="__main__":
    main()



























