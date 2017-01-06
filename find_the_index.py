list_a = ["Ali", "Ali", "Atalay", "Samet", "Mehmet", "Sila", "Irem", "Ali"]
L = []
c = 0
i = 0
name = input("Enter the name to find its index : ")
while i < len(list_a):
    if list_a[i].lower() == name.lower():
        L.append(c)
    c += 1
    i += 1
if len(L) == 0:
    print("There is no such name on the list...")

print(L)
