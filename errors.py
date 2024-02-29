# All errors have been fixed and comments indicate correction
 


print ("Welcome to the error program")
#syntax error: error was due to missing parentheses
print("\n")
#syntax error: error was due to missing parentheses and indentation'''

# Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = 24
#syntax error : age_str should have a single "=", 24 years old should be "24" to be recognised as an integer
age = int(age_Str) 
print("I'm " + str(age) + " years old.")
#logical error : age should be cast to a str

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5
total_years = age + years_from_now
#synthax error: age is not defined
print ("The total number of years:" + str(total_years))
#synthax error: "answer_years" is undefined, "total_years" should be cast to a string
#synthax error: there should be parentheses after the print statement

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12
#runtime error
print ("In 3 years and 6 months, I'll be " + str(total_months) + " months old")
#total_months should be cast to a string
#HINT, 330 months is the correct answer