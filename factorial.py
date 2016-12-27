num = int(input("Enter a number"))

factorial = 1
while num > 1:
    factorial *= num

    num -= 1
print(factorial)
