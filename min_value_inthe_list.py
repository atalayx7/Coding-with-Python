def min_value(L):
    '''L is a list of ints that are >= -1. Return the minimum value in L that is > -1. If L doesn't have any value in it other than -1, return -1.
    '''

    minimum = -1

    for i in L:
        if i < minimum or minimum == -1:
            minimum = i
    return minimum


list1 = [10, 4, 5, -3, -7, 12, 11]
print(min_value(list1))
