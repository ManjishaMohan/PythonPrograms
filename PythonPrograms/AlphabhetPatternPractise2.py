'''
     A
   A B C
  A B C D
 A B C D E
A B C D E F G
'''

for i in range(1,6):
    for j in range(1,(2*i-1)+1):
        print(" "*(6-i) + str(j),end="")
    print("")
