'''
Welcome to ICICI bank
Please enter your name:
Please enter your account number:
Choose one of the options:
1. Press 1 to deposit:
2. Press 2 to withdraw:
3. Press 3 to exit

1
How much money you want to deposit: 60000
Okay, transaction completed.
Updated balance: 60000'''

print("Welcome to Starling Bank")
name=input("enter your name :")
account_number=int(input("enter your account number :"))
print("Choose one of the options:\n Press 1 to deposit:\n  Press 2 to withdraw: \n Press 3 to exit")
option=int(input("enter the option :"))

class Bank:

    balance=20000
    def deposit(self, amountdeposit):
            print("enter the amount to deposit :")
            updated_amount=self.balance+self.amountdeposit
            print("your updated deposit is :", updated_amount)

    def withdraw(self, withdrawamount):
            print("enter the amount to withdraw :")
            withdraw_amount=self.balance-self.withdrawamount
            print("your updated saving is :", withdraw_amount)

    def exit(self):
            print("thank you for using starling bank")

obj=Bank()
if(option == 1):
    obj.deposit()
elif(option == 2):
    obj.withdraw()
elif(option == 3):
    obj.exit()