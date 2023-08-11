'''amount1=int(input("Enter the first amount in Celsius:"))
amount2=int(input("Enter the last amount in Celsius:"))

fahrenheit1=amount1 * 9/5 + 32
fahrenheit2=amount2 * 9/5 + 32

print( "CELSIUS= " ,fahrenheit1,	"FAHRENHEIT=",fahrenheit2)'''

celsius_First = int(input("Enter the first amount in Celsius: "))
celsius_Last = int(input("Enter the last amount in Celsius: "))
for i in range(celsius_First, celsius_Last + 1):
    print(i, (i * 9 / 5 + 32))
