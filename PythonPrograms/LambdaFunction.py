
#using function
def f(x):
    return x**2
print(f(8))

# using lambda
g =lambda x:x**2
print(g(8))
#filter function

#Map function
def addtion(n):
    return n+n
numbers=(1,2,3,4,5)
result=map(addtion,numbers)
print(list(result))
#sort function