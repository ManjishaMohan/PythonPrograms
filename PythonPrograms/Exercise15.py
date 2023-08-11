#Body Mass index (BMI)
weight=float(input("Enter your weight in (kg) = "))
height=float(input("Enter your height in (m) = "))
bmi=weight/(height*height)
if(bmi<=18.5):
    print("Your BMI is:",round(bmi,2))
    print("You are in the “Underweight” range")
elif(bmi>18.5 and bmi<=24.9):
    print("Your BMI is:", round(bmi,2))
    print("You are in the “Normal” range")
elif(bmi>25 and bmi<=29.9):
    print("Your BMI is:", round(bmi,2))
    print("You are in the “Overweight” range")
elif(bmi>=30):
    print("Your BMI is:", round(bmi,2))
    print("You are in the “Obese” range")