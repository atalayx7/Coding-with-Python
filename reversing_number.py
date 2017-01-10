x = int(input("Enter a number : "))
while x > 0:
    a = x % 10
    print(a, end="")
    x = x - a

    x = x // 10
