salary=int(input("Enter your Salary: "))
experience=int(input("Enter your experience: "))

if(experience>5):
    salary=salary+5/100
    print("eligilble for Bonus")
    print(salary)
elif(experience<5):
    print("not eligible")