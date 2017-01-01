def hide_vowels(s):
    """ (str) -> str
    Return an updated version of s where vowels (a,e,o,u,i) are replaced
    by dashes (-).          Assumption: s contains only lowercase letters.
    hide_vowels('same')
    's-m-'
    hide_vowels('ymc')
    'ymc'
    """
    vowels = "aeiou"
    a = ""
    for i in s:
        if i in vowels:
            a += "-"
        else:
            a += i
    return a


s = input("Enter a string : ")
print(hide_vowels(s))

# gp
