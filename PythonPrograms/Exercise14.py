age=int(input("Enter your age:"))
if(16<age and age<60):
    print("Your ticket costs £6.00")
elif(age<=16):
    print("Your ticket costs £3.00")
elif(age>60):
    print("Your ticket costs £2.00")