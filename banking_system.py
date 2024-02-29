# A mock banking system that deposits and withdraws funds.
correct_userame = "joy"
correct_password = "pass123"

balance = 0.0
logged_in = False
while not logged_in:
    #Get the username and pasword 
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_userame and password == correct_password:
        print("Login successful!\n")
        logged_in = True
    else:
        print("Incorrect username and password. Please try again!")

while True:
    try:
        print(f"Hi {username}, your current balance is ${balance}")
        print('''
            1 -Deposit Funds
            2- Withdraw Funds
            3 -Exit
            ''')
        
        choice = input("Choose your option: ")
        if choice == "1":
            #ask for input from user
            amount=float(input("Enter the deposit amount: "))
            #Add balance
            balance += amount
            #print new balance
            print(f"Deposit successful. Your new balance is ${balance:,}")
        elif choice == "2":
            #Ask for the amount to withdraw
            amount = float(input("Enter the amount to withdraw: "))
            #check amount is not greater than balance
            if amount > balance:
                print("Insufficient funds. Withdrawal cancelled \n")
            else:
                balance -= amount  #Deduct the amount from the balance
                print(f"Withdrawal successful. Your new balance is ${balance:,} \n")
        elif choice == "3":
            print(f"Cheers {username}, Come again!")#print new balance
            break
        else:
            print("Invalid choice. Enter option 1/2/3. \n")
    except:
        (print("There's something wrong with your input ")) 