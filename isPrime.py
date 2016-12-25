number = int(input("Enter a number : "))

if number > 1:
    for i in range(2, number):
        if number % i == 0 and number != 2:
            print("This is not prime.")
            break
    else:
        print("This is prime.")

else:
    print("The number must be more than 1.")
