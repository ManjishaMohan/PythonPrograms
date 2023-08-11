

# creating identical list by using list comprehenshion
a=[10,20,30]
b=[x for x in a]
print(b)

# creating a list within range from 1200 to 2000

b=[x for x in range(1200,2000,130)]
print(b)

# adding 6 to list
a=[10,20,30]
b=[i+6 for i in a]
print(b)

age = [16,24,26,45,60]
new_age = [i+6 for i in age]
print(new_age)

'''Using list comprehension, construct a list from
the squares of each element
in the list, if the square is greater than 50.'''
#----------------------------------------------------
'''
Given dictionary is consisted of vehicles and their weights 
in kilograms. Construct a list of the names of vehicles with 
weight below 5000 kilograms. In the same list comprehension
 make the key names all upper case.
'''

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

weight=[ i.upper() for i in dict if dict[i]<5000]
print(weight)
lst = [i for i in dict if dict[i]<5000]
print(lst)

