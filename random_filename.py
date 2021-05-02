import random
import string

filename= "".join([random.choice(string.ascii_lowercase) for _ in range(random.randint(7,15))]) #The length is up to you

print(filename)

#It creates a random file name
