def is_palindrome(word):
    """ (str) -> bool    A string is a palindrome if it reads the same in both directions.
  Some examples of palindrome are ‘civic’, ‘racecar’, ‘deed’, ‘eye’     
  Return True if s is a palindrome              
  >>> is_palindrome('dead')         
  False        
  >>> is_palindrome ('civic')         
  True     
  """
    a = ""

    for i in range(len(s), 0, -1):
        a += s[i - 1]
    if a == s:
        return True

    else:
        return False


s = input("Enter a string : ")
print(is_palindrome(s))
