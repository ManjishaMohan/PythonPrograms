number1=int(input("Enter first number :"))
number2=int(input("Enter first number :"))
press1=int(input("Enter numbers from 1 to 4 :"))

def add(number1,number2):
    add=number1+number2
    if (press1 == 1):
     print("Addition of 2 numbers :",add)

add(number1,number2)

def multiply(number1,number2):
    multiply=number1*number2
    if(press1 == 2):
     print("multiplication of 2 numbers :",multiply)

multiply(number1,number2)

def divide(number1,number2):
    divide=number1/number2
    if (press1 == 3):
     print("division of 2 numbers :",divide)

divide(number1,number2)

def modulas(number1,number2):
    modulas=number1%number2
    if (press1 == 4):
     print("modulas of 2 numbers :",modulas)
    else:
       print("wrong press")
modulas(number1,number2)





