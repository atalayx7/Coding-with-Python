a = "000"
b = "001"
c = "010"
d = "011"
e = "100"
f = "101"
g = "110"
h = "111"

"""
osr2 text file  contains: 
0010111011000010000001000011111011000010001111011101011010111100001000110001
0011101111010011001011000010111000010000010111000000110000011110101111010011
1110111000001001001010101011000011101000001011011101000100001100000011001100
001000010100
"""
finallist = []
with open("osr2.txt", "r") as x:
    x = x.read()
    n = 3
    thelist = ([x[i:i+n] for i in range(0, len(x), n)])

    for i in thelist:
        if i == "000":
            finallist.append("001")

        elif i == "001":
            finallist.append("010")

        elif i == "010":
            finallist.append("111")

        elif i == "011":
            finallist.append("100")

        elif i == "100":
            finallist.append("101")

        elif i == "101":
            finallist.append("110")

        elif i == "110":
            finallist.append("011")

        elif i == "111":
            finallist.append("000")


print(finallist)
t = ("".join(i for i in finallist)) 
print(t)
print(''.join(chr(int(t[i*8:i*8+8], 2)) for i in range(len(t)//8)))  #binary to text
