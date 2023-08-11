'''# a file named "geek", will be opened with the reading mode.
file = open('C:/Users/Manjisha/Desktop/hello.txt', 'r')
# This will print every line one by one in the file
for each in file:
    print (each)'''
''' 
# Python code to illustrate read() mode
file = open("Manji.txt", "r")
print (file.read())

# Python code to create a file
file = open('Manji.txt','a')
file.write("This is the append command")
file.write("It allows us to append in a particular file")
file.close()'''
# Python code to illustrate with() alongwith write()
with open("file.txt", "w") as f:
    f.write("Hello World!!!")

# split()
#split() function
with open("C:/Users/Manjisha/PycharmProjects/pythonProject2/Manji.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
#length
with open("Manji.txt", "r") as file:
    data = file.read()
    no_of_chars = len(data)
    print (no_of_chars)





