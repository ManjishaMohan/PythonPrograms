quantity=int(input("Enter the quantity:"))
cost=quantity*100
if(cost>1000):
    print("cost",cost)
    print("Eligible for 10% Discount")
else:
    print("cost", cost)
    print("sorry discount is not applicable")