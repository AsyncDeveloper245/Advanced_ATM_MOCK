import random
from datetime import datetime as dt
import time


def account_number():
    return random.randrange(1000000000, 30000000000)


def account_login(get_login_method,users):
    if get_login_method == 1:
        print('Welcome please login below')
        username = str(input('Username: '))
        password = str(input('Password: '))
        print('Wait, while we verify your details.....')
        if username in users.keys():
            if password == users[username]['password']:
                print('*' * 100)
                print("10% .\n\n35% ..")
                time.sleep(2)
                print("\n50% ...\n\n70% ....")
                time.sleep(2)
                print("\n90% ......\n\n99% .......")
                time.sleep(1)
                print(
                    f"Welcome {username},\nAccount Balance: #{users[username]['balance']}\n{dt.today().strftime('%d %b %Y')}\nAccount Number:{users[username]['account_number']}")
                print('-' * 100)
                print(
                    f'[{users[username]["account_number"]}]Choose From the options below\n 1.Withdraw cash\n 2.Deposit Cash\n 3.Make Complaints')
                get_transaction_status = int(input('>> '))
                handle_transaction(get_transaction_status, users, username)
            else:
                print("Invalid Credentials")
        else:
            print("Invalid Credentials")

        return username, password


def account_signup(get_login_method):
    if get_login_method == 2:
        print('Welcome, Guest\nFill in the form below ')
        username = str(input('Username: '))
        password = str(input("Password: "))
        account_no = account_number()
        print('Do you want to submit [y/n]')
        submit_response = input('[y/n]: ')
        if submit_response == 'y':
            username, password,account_no = username, password,account_no
            print(f"{username.title()} Registration Successful with Account Number {account_no}")
        elif submit_response == 'n':
            print('You can login if you already have an account.\nThank you')
        else:
            print('Please check your input')

        return username,password,account_no


def handle_transaction(get_transaction_status, users, username):
    if get_transaction_status == 1:
        print('How Much do you want to withdraw?')
        withdraw_amount = int(input('Enter Amount to withdraw: '))
        print("press 'y' to confirm and 'n' to abort")
        withdraw_approve = str(input('[y/n] >> '))
        if withdraw_approve == 'y':
            if withdraw_amount > users[username]['balance']:
                print('You have insufficient balance')
                account_login(1,users)
            else:
                users[username]['balance'] -= withdraw_amount
                print(f"Take Your cash")
                account_login(1, users)
        else:
            print('Thank you,Try Again')
            account_login(1,users)

    elif get_transaction_status == 2:
        print('How much would you like to Deposit')
        deposit_amount = int(input('>> '))
        print("press 'y' to confirm and 'n' to abort")
        deposit_approve = str(input(('[y/n] >> ')))
        if deposit_approve == 'y':
            users[username]['balance'] += deposit_amount
            print(f'you have just deposited {deposit_amount}\n your new account balance: #{users[username]["balance"]}')
            account_login(1, users)

    else:
        print('What issue would you like to report')
        user_complaint = str(input('>> '))
        users[username]['user_complaint'] = user_complaint
        print('Thank you for contacting us')
        account_login(1, users)


def main():
    users = {'admin': {'balance': 0, 'password': 'admin','account_number':1234586555}}
    print('Welcome to TheAsyncWorld. \npress 1 to login.\npress 2 for registration')
    get_login_method = int(input(">> "))
    if get_login_method == 1:
        account_login(get_login_method,users)


    else:
        username,password,account_no=account_signup(get_login_method)
        users[username]= {}
        users[username]['password']=password
        users[username]['balance']=0
        users[username]['account_number']=account_no
        account_login(1,users)


if __name__ == "__main__":
    main()
