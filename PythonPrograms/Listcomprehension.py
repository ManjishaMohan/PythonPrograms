
S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print(S)
print(V)
print(M)

# list with pop
age=[10,45,23,56,78]
result=age.pop()
age.pop()
age.pop()
age.pop()
age.pop()
age.pop()
print(age)
