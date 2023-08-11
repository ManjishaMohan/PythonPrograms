

num1=10
num2=2

try:
    divide=num1/num2
    print(divide)
except ZeroDivisionError:
    print("executed")
else:
    print("executed only when their is no exception")
finally:
    print("executed in both situation - exception and no exception")