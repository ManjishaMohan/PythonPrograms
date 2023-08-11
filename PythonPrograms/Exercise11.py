
#input
first_name=input("enter the first name :- ")
second_name=input("enter the second name:- ")
#upper case
first_name = first_name.upper()
second_name = second_name.upper()
print("Your full name is ", first_name,second_name)
#initials
print("Your initials are ", first_name[0],second_name[0])
#length function
print("First name length is",len(first_name),"letters")
print("Last name length is",len(second_name),"letters")
print("Full name length is",(len(first_name)+len(second_name)),"letters")
# first letter starts and ends
print("First name starts with",first_name[0])
print("First name ends with ",first_name[-1])
print("Last name starts with",second_name[0])
print("Last name ends with",second_name[-1])

#indexes
print("First name indexes are","0 - ",(len(first_name)-1))
print("last name indexes are 0 - ",(len(second_name)-1))
# trim
print("First name trims 1 ",first_name[0:3])
print("First name trims 2 ",first_name[3:10])
print("Last name trims 1 ",second_name[0:3])
print("Last name trims 1 ",second_name[3:10])



