'''A list is called a palindrome if the sum of the numbers of the two halves are the same. Write this function:
is_palindrome(list): returns True if the list is palindrome
Sample run:
is_palindrome([2, 3, 3, 2, 1, 4, 5, 0])
True
Explanation: 2+3+3+2 == 1+4+5+0
'''


def is_palindrome(list1):
    a = len(list1) // 2
    b = 0
    c = 0
    for i in range(a):
        b += list1[i]
    for i in list1[a:(len(list1))]:
        c += list1[i]

    if c == b:
        return True
    else:
        return False


print(is_palindrome([2, 3, 3, 2, 1, 4, 5, 0]))

print(is_palindrome([2, 3, 3, 2, 1, 4, 5, 1]))
