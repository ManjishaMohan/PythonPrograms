
'''wap to create a function which takes string input, calculates
the length, vowels, constonants '''

x=input("Enter the string :")
def alphabhets(x):
    print("length of the string :", len(x))
    vowels = 0
    consonants = 0
    for i in x:
       if(i=="a" or i=="e"or i=="i" or i=="o" or i=="u" or
       i =="A"or i =="E"or i =="I"or i =="O"or i =="U" ):
        vowels=vowels+1
       else:
         consonants=consonants+1
    print("number of vowels", vowels)
    print("number of consonants ",consonants)

alphabhets(x)