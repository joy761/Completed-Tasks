''' Write code to request input from user
store input in a variable called "age"
if the user inputs 40 or over, print "You're over the hill"
assume that the oldest someone can be is 100. if the user enters a higher number, output "sorry you're dead"
if the user is 65 or older, output the message "Enjoy your retirement!" 
if the user is under 13, output the message "You qualify for the kiddie discount 
if the user is 21, output the message "congrats on your 21st!" 
for any other age, output "age is but a number'''

age = int(input("What is your age? "))

if age >= 40:
    print("You're over the hill ")
    
if age > 100:
    print("Sorry you're dead!")

if age >= 65:
    print("Enjoy your retirement!")

elif age < 13:
    print("You qualify for the kiddie discount.")

if age == 21:
    print("Congrats on your 21st!")

else:
    print ("Age is but a number")

