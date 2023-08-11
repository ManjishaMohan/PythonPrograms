

num_one=int(input("enter the first number :"))
num_two=int(input("enter the first number :"))

try:
    answer=num_one//num_two
    print(answer)
except:
    print("Sorry ! try again  ")


age=[10,20,30,40]
try:
   print(age[4])
except:
    print("can't access this index")