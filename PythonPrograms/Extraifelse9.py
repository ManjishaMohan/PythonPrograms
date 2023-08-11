medicalcause=str(input("Do you have any medical cause (Y or N) : "))

if(medicalcause.upper()=="Y"):
    print("Student is not allowed to sit in exam")
elif(medicalcause.upper()=="N"):
    print("Student is allowed to sit in exam")