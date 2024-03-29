
user_one = {
    'full_name':'SpongeBob Squarepants', 
    'user_name':'krusty krab', 
    'password':'pineapple', 
    'account_balance': 750000, 
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
    'account_balance':900000, 
    'connected_banks': [
    ("First Federal National Bank", 50000), 
    ("Chase", 19000),
    ("Guaranty Bank & Trust", 250000),
    ]
    
 }
print()
print(f"Welcome, {(user_one['full_name'])}!")
print()
user_name_prompt = input("Please enter your user name: ")
while user_name_prompt != (user_one['user_name']):
    print("User name is incorrect! Please enter the correct user name.")
    user_name_prompt = input("Please enter your user name: ")
password_prompt = input("Please enter your password: ")
print()
while password_prompt != (user_one['password']):
    print("Your password is incorrect! Please enter the correct password.")
    password_prompt = input("Please enter your password: ")
if password_prompt == (user_one['password']):
    print(f"You're current balance is ${user_one['account_balance']}")
print()
print("The available funds from your connected accounts are as follows:")
print()
bank_one = user_one['connected_banks'][0]
bank_two = user_one['connected_banks'][1]
bank_three = user_one['connected_banks'][2]
banks = bank_one, bank_two, bank_three
for x, y in banks:
    print(f"{str(x)}: ${str(y)}")
print()
transfer = input(f"Would you like to transfer money to {user_two['full_name']} (y/n)? ")
print()
while transfer == "y":
    amount = int(input("How much would you like to transfer? (Whole dollars only, please!) "))
    print()
    if amount > user_one['account_balance']:
        print("You have insufficent funds. Please, try another amount.")
        print()    
    elif amount < user_one['account_balance']:
        print("Beginning transaction.....")
        print()
        print(f"Your transaction was successful! ${amount} will be transferred to {user_two['full_name']}")
        print()
        user_one['account_balance'] -= amount
        amount += user_two['account_balance']
        transfer = input(f"Would you like to make another transfer to {user_two['full_name']} (y/n)? ")
        print()
        if transfer == "n":
            print(f"Your remaining balance is ${ user_one['account_balance']}")
            print()
else:
    print("That will end this transaction. Have a great day!")





 
