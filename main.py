
user_one = {
    'full_name':'SpongeBob Squarepants', 
    'user_name':'krusty krab', 
    'password':'pineapple', 
    'account_balance': '750000', 
    'connected_banks': [
        ("RBFCU", 10000), 
        ("Pioneer Bank", 25000), 
        ("Wells Fargo", 100000)
    ] 
}

user_two = {
    'full_name':'Sandy Cheeks', 
    'user_name':'treedome', 
    'password':'karate', 
    'account_balance':'900000', 
    'connected_banks': [
    ("First Federal National Bank", 50000), 
    ("Chase", 19000),
    ("Guaranty Bank & Trust", 250000),
    ]
    
 }

user_name_prompt = input("Please enter your user name: ")
while user_name_prompt != (user_one['user_name']):
    print("User name is incorrect! Please enter the correct user name.")
    user_name_prompt = input("Please enter your user name: ")
password_prompt = input("Please enter your password: ")
while password_prompt != (user_one['password']):
    print("Your password is incorrect! Please enter the correct password.")
    password_prompt = input("Please enter your password: ")
if password_prompt == (user_one['password']):
    print(f"You're current balance is ${user_one['account_balance']}")

bank_one = user_one['connected_banks'][0]
bank_two = user_one['connected_banks'][1]
bank_three = user_one['connected_banks'][2]
banks = bank_one, bank_two, bank_three
for x, y in banks:
    print(f"{str(x)}: ${str(y)}")

user_prompt = input(f"Would you like to proceed to transfer money to {user_two['full_name']}? ")
while user_prompt == "y":
    user_prompt = input("How much would you like to transfer? ")
    if user_prompt > user_one['account_balance']:
            print("You have insufficent funds. Try another amount.")
            user_prompt = input("How much would you like to transfer? ")
    if user_prompt < user_one['account_balance']: 
        print(f"${user_prompt} will be transferred to {user_two['full_name']}.")
        new_acct_bal_one = ((int)(user_one['account_balance']) - (int)(user_prompt))
        print(new_acct_bal_one)
        new_bal = new_acct_bal_one - (int)(user_prompt) #How do I get this to loop? 
        print(new_bal)
        #new_acct_bal_two = ((int)(user_prompt)(int)(user_two['account_balance']) + (int)(user_prompt))
        user_prompt = input("Would you like to make another transfer? ") 
    else: 
        print(f"Balance: {(int)(user_one['account_balance'])} ")
        print("That will end this transaction. Have a great day!")  #Need these two lines to print when saying no after several transfers.     
if user_prompt == "n":
            #print(f"Balance: {(int)(user_one['account_balance'])} ")
            print("That will end this transaction. Have a great day!") #Need this to print only when saying no to transferring to Sandy Cheeks.

#Need to be able to print the correct balance after making transfers. 