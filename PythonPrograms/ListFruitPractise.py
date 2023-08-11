
[] #empty list

fruit=["mango","apple","watermelon"]
print(type(fruit))

# to replace something
fruit[1]='banana'
print(fruit)

# to delete something
del fruit[1]
print(fruit)

#len() function is used to get the length of a list
print(len(fruit))

# to insert something
fruit.insert(0,"Apple")
print(fruit)

# to append something- will insert new value at last
fruit.append("pear")
print(fruit)

# to sort
fruit.sort()
print(fruit)

# to reverse something
fruit.reverse()
print(fruit)


