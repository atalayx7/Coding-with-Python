# Write a function that counts the number of times a substring occurs in a string
def count_occurrence(str1, str2):
    ''' (str, str - > int)
    Return the number of times str1 appears in str2.
    >>>count_occurrence('ana', 'banana')
    1
    >>>count_occurrence('es','messages')
    2
    >>>count_occurrence('tim', 'course')
    0
    '''
    count = 0
    for i in range(0, len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]:
            count += 1
    return count


num = count_occurrence('ur', 'course')
print(num)
