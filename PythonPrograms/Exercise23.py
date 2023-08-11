print("Try and name 4 actors who have played James Bond.")
attempt = 1
count=0
while(attempt<5):
    name = input("Name an actor:=")
    if (name.lower() == "roger moore"):
        print("Well done: Roger Moore was Bond in Live and Let Die.")
        attempt = attempt+1
        count=count+1
    elif(name.lower() == "seanconnery"):
        print("Well done: Sean Connery was Bond in From Russia with Love")
        attempt = attempt +1
        count=count+1
    elif(name.lower()=="pierce Brosnan"):
        print("Well done: Pierce Brosnan was Bond in From Die Another Day")
        attempt = attempt + 1
        count = count + 1
    elif(name.lower() == "daniel craig"):
        print("Well done: Daniel Craig was Bond in Skyfall.")
        attempt = attempt + 1
        count=count+1
    else:
        print("Sorry,", name,"hasn’t played Bond as far as I know.")
        attempt= attempt+1
print("you got",count, "out of 4")

