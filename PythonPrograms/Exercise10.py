individual_cost=int(input("Enter total number of individuals :"))
under_sixteen=int(input("Enter total number of under 16s:"))
families=int(input("Enter total number of families :"))
cost=individual_cost*68
sixteen=under_sixteen*32.25
families_cost=families*42.75
print("Category Price Breakdown:")
print("Price is",cost,"for",individual_cost,"individuals" )
print("Price is",sixteen,"for",under_sixteen,"16s")
print("Price is",families_cost,"for",families,"families" )
total_member=individual_cost+under_sixteen+families*4
total_price=cost+sixteen+families_cost
print("Total Persons are",total_member)
print("Total Event Price is",total_price)
print("More info and booking visit our website")