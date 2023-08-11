
# for loop
'''for i in range(0,1): # rows
    for j in range(0,6): # columns
        print("*" * j)'''
 # while loop
'''i=0
j=0
while(i<1):
    while(j<6):
        print(j * "*")
        j=j+1
        i=i+1'''
# reverse - for loop
'''for i in range(1,0,-1):
    for j in range(6,0,-1):
        print(j*"*")'''
#reverse - while loop
'''i=1
j=6
while(i>0):
    while(j>0):
        print(j*"*")
        i=i-1
        j=j-1'''

for i in range(1,5):
    for j in range(1, i+1):
        print(j, end =' ')
    print(' ')



