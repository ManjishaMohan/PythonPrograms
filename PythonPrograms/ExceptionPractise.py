
#try except finally else raise
num1=10
num2=2
try:
    age = [45, 34, 21, 44, 23]
    print(age[5])
except IndexError:
    print("Element not present")
try:
    divide=num1/num2
    print(divide)
    fhand=open("avinash.txt")
except ZeroDivisionError:
    print("Sorry, division by 0 not allowed, please use proper numbers")
except IndexError:
    print("Element not there")
except Exception:
    print("Something went wrong")
