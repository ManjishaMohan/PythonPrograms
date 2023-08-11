
'''
wap to create a function which takes weight and height of the
   user . bmi: ->
'''
weight=float(input("Enter your weight : "))
height=float(input("Enter your height :"))
def bmi(weight,height):
    bmi_calculation=weight/(height*height)
    print("Your BMI is :",round(bmi_calculation,2))
    if bmi_calculation<18.5:
        print("You are in the “underweight” range")
    elif 18.5<bmi_calculation<24.9:
        print("You are in the “Normal” range")
    elif 25<bmi_calculation<29.9:
        print("You are in the “Overweight” range")
    elif bmi_calculation>=30:
        print("You are in the “Obese” range")

bmi(weight,height)
