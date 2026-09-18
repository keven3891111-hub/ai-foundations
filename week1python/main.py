def demo():
    for n in [1, 2, 3]:
        if n == 2:
            return n

        print(n)

    print("循环之后")
    return 99


result = demo()
print("接收到：", result)