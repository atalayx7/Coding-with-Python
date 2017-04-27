dailySpending = [4.59, 13.24, 0, 0, 2.5, 24.74, 1.3,
                 31.5, 1.8, 24.74, 10.5, 1, 8.64, 1, 3.8]

total = 0.0
count = 0
for i in range(len(dailySpending)):
    total += dailySpending[i]
    count += 1

print("Total expense during", count, "day : %.02f" % total, " €")
print("The average in a day : %.02f" % (total / count), " €")
