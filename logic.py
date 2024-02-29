Rent_years = "10"
#Logical error: "10" This should be an integer, not a string. The code will run,but not with the expected output
months_lived = Rent_years * 12

print(f"You have live here for " + str(months_lived) + " months") 