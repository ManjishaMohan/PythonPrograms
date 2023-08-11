classheld=30
print("Number of classes held :",classheld)
attended=int(input("Number of classes attended:"))
percentage=attended/classheld*100
print(round(percentage,2))
if(percentage>=75):
    print("student is allowed to sit in exam ")
else:
    print("student will not be allowed to sit in exam ")