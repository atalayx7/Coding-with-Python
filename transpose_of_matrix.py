def transpose(l):
    l2 = []
    for i in range(len(l[0])):
        l2.append(len(l) * [0])

    for i in range(len(l)):
        for j in range(len(l[0])):
            l2[j][i] = l[i][j]
    return l2


l = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print(transpose(l))
