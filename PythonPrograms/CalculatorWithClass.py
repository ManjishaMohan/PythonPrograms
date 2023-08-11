
class Calculator:
    print("Press 1 for addition \nPress 2 for subtract \nPress 3 for multiply \nPress 4 for divide ")
    oper = int(input("Enter the operation to be perform :"))
    if (oper == 1):
        def sum(self):
            num1 = int(input("Enter The first number :"))
            num2 = int(input("Enter The second number :"))
            sum = num1 + num2
            print("The addition will be ", sum)

    elif (oper == 2):
        def subtract(self):
            num1 = int(input("Enter The first number :"))
            num2 = int(input("Enter The second number :"))
            sub = num1 - num2
            print("The substraction will be ", sub)


    elif (oper == 3):
        def multiply(self):
            num1 = float(input("Enter The first number :"))
            num2 = float(input("Enter The second number :"))
            mul = num1 * num2
            print("The multiplication will be ", mul)

obj=Calculator()
obj.sum()
obj.multiply()
obj.subtract()


class Calculator:
    def sum(self):
        num1 = int(input("Enter The first number :"))
        num2 = int(input("Enter The second number :"))
        sum = num1 + num2
        print("The addition will be ", sum)

    def subtract(self):
        num1 = int(input("Enter The first number :"))
        num2 = int(input("Enter The second number :"))
        sub = num1 - num2
        print("The substraction will be ", sub)

    def multiply(self):
        num1 = float(input("Enter The first number :"))
        num2 = float(input("Enter The second number :"))
        mul = num1 * num2
        print("The multiplication will be ", mul)

    def divide(self):
        num1 = float(input("Enter The first number :"))
        num2 = float(input("Enter The second number :"))
        div = num1 / num2
        print("The Division will be ", div)


obj = Calculator()
obj.sum()
obj.subtract()
obj.multiply()
obj.divide()
