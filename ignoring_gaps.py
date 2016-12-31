s = "Today     is         Tuesday"
i = 0
while s.find(" ", i) != -1:

    print(s[i: s.find(" ", i)])

    i = s.find(" ", i) + 1

    while s[i] == " ":
        i += 1
print(s[i:])
