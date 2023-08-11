'''
def factorial(x):
    if x==1:
        return x
    else:
        return(x*factorial(x-1))
num=2
print("factorial of number",num ,"is", factorial(num))'''
''' 
def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0]+list_sum(num_list[1:])

print(list_sum([2,4,5,6,7]))'''

x=4
def func():
    global x
    x=1
    print(x)
func()
print(x)

