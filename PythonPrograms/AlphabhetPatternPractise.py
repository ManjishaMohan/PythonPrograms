

'''
A
A B C
A B C D
A B C D E
'''

''' ASCI code 
65-A
66-B
67-C
68-D
69-E
70-F   
'''
for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end=" ")
    print(" ")
