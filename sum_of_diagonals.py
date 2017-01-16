def sum_diagonals(L):
    '''L is a list of lists of ints. All of L's sublists have the same length which is equal to the length of L (L represents a square matrix). Return a new list that contains the sum of diagonals --there are two diagonals. For example, for the list [[5, 10, 15], [1, 2, 3], [10, 20, 30], return [37, 27].
    '''
    size = len(L)
    sum_diag1 = 0
    sum_diag2 = 0
    j = size - 1
    for i in range(0, size):
        sum_diag1 += L[i][i]
        sum_diag2 += L[i][j]
        j -= 1
    return sum_diag1, sum_diag2


L = [[5, 10, 15], [1, 2, 3], [10, 20, 30]]
print(sum_diagonals(L))
