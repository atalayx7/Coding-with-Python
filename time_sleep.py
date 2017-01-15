import time

run = input("Start? Please Type 'start' > ")
second = 0
# Only run if the user types in "start"
if run == "start":
    while True:
        print(">>>>>>>>>>>>>>>>>>>", second)

        time.sleep(5)
        # Sleep for five second
        second += 1
        # Increment the second total
