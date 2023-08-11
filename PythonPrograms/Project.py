
# Random password generator

import random
import re #regular expression - the functions in this module let you check if a particular string matches a given regular expression
import numpy as np
def email():
    email = input("Enter the Email Id:")
    match = re.search(r'[\w]+@[\w]+.\w+', email)

    if match:
        print("valid email !! ", match.group())
    else:
        print("not valid !! ")
email()

print("Some suggestion to create the strong Password ! ")
password = int(input("Enter the length of password : "))
print(password)
while(password < 4):
    input("length must be minimum 4 : ")
    print("sorry try again !")
    break
else:
    s = "abcdefghijklmnopqrstuvwxyz"
    pass1 ="".join(random.sample(s,password-3))
    j="01234567890"
    pass2 ="".join(random.sample(j,1))
    k="!@#$%^&*()?"
    pass3 ="".join(random.sample(k,1))
    d="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pass4 ="".join(random.sample(d,1))
    m = pass1+pass2+pass3+pass4
    print("Your Password : ",m)

print("To maintain your account's safety Make use of the Secure Password ! ")
