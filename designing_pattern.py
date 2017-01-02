def patterns(num_rows, num_cols):
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            if (i + j) % 2 == 0:
                print("*", end="")
            else:
                print(".", end="")
        print()


num_rows = int(input("Enter the row length : "))
num_cols = int(input("Enter the column length : "))
(patterns(num_rows, num_cols))
