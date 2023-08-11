#Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.
#Sample string : 'w3resource'
#Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}

string=input("enter the string:- ")
dict={}
for x in string:
    if x in string:
        x += 1
    else:
        x = 1
print(dict)