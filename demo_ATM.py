'''
Author:Bichu Sasi
Date:28?10/2024
Description: Write a program that simulates a simple bank ATM system. The user has an initial balance of $1000. The ATM should display a menu with options to.
'''

balance_amount=1000
while True:
    print("1./tCheck Balance")
    print("2./tDeposit Money")
    print("3./tWithdraw Money")
    print("4./tExit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(f"The current balance ${balance_amount}")
    elif choice==2:
        deposit_amount=float(input("Enter the amount:"))
        balance_amount += deposit_amount
        print(f"The deposit amount:${deposit_amount} and The current balance:{balance_amount}")
    elif choice==3:
        withdraw_amount=float(input("Enter the amount:"))
        if balance_amount<withdraw_amount:
            print("insufficient balance")
        else:
            balance_amount -= withdraw_amount
            print(f"The withdrawn amount:${withdraw_amount} and The current balance:{balance_amount}")
    elif choice==4:
        break
    else:
        print("Invalid choice!")