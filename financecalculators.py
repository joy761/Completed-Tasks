import math

#request input from user, user should be allowed to choose which calculation they want to do "investment" or "Bond"
#calculate bond or investment, based on users input.

#option for users
investment = "To calculate the amount of interest you will earn on your investment"
bond = "To calculate the amount you will have to pay on a home loan"

#casefold removes case sensitivity hence user's input can be with or without caps

print("investment = To calculate the amount of interest you will earn on your investment")
print("bond = To calculate the amount you will have to pay on a home loan")
print("Enter either 'investment' or 'bond' from the menu below to proceed:")

options = input ("Please enter'investment' or 'bond': ")
#if user inputs "investment" they need to input the following:

if options.casefold() == "investment":

    investment_deposit = int(input("How much is your deposit?"))
    investment_rate = int(input("Enter interest rate: "))
    investment_years = int(input("How many years do you plan on investing? "))
    interest = input("Enter either 'simple' or 'compound' interest': ")
    
    if interest.casefold() == "simple":
        simple_interest = investment_deposit *(1 + (investment_rate/100) * investment_years)
        print(f"you will make {simple_interest} on your investment")
    
    elif interest.casefold() == "compound":
        compound_interest = investment_deposit * math.pow((1+(investment_rate/100)), investment_years)
        print(f"You will make {compound_interest} on your investment")
   

elif options == "bond":
#user inputs info needed to calculate bond

    bond_value= int(input("Please enter present value of the house : "))
    annual_interest = int(input("Enter interest rate: "))
    bond_months= int(input("Enter number of months to repay bond: "))
    monthly_interest = (annual_interest / 100) / 12
    bond_repayment = (annual_interest * bond_value) / (1-(1 + monthly_interest) ** (- bond_months))
    print(f"you will repay {bond_repayment}.")
else:
    print("Error! input investment ot bond")
 