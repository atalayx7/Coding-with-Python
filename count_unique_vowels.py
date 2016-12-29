# Write a function that counts the number of times a substring occurs in a string
def count_unique_vowels(s):
    ''' (str - > int)
    Return the number of unique vowels in s.
    >>>count_unique_vowels("apple")
    2
    >>>count_unique_vowels("banana")
    1
    '''
    seen = ""
    for ch in s:
        if ch not in seen and ch in "aeiou":
            seen += ch
    return len(seen)


num_unique = count_unique_vowels("apple")
print(num_unique)
