
#Python program to check whether a string is palindrome or not:

string = input("enter the string :-")

if string == string[:: - 1]:
    print( "yes , its a palindrome")
else:
    print("No , not a palindrome")
