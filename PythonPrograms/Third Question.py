
radius=int(input("Enter the radius  :- "))

def areaOfcircle():
    area = round(22/7 * radius * radius, 2)
    circumference =round(2 * 22/7 * radius, 2)
    print("area of circle", area ,"\n" ,"circumference :-",circumference)
areaOfcircle()
