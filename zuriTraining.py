from datetime import datetime as dt
import random

def generate_account_number():
    pass
def account_login():
    try:
        get_login_method = int(input('>> '))
        if get_login_method == 1:
            print('Welcome please login below')
            username = str(input('Username: '))
            password = str(input('Password: '))
            print('Wait, while we verify your details.....')
            if username in users.keys():
                if password == users[username]['password']:
                    print('Login Successful')
                    print('*' * 100)
        return  username,password
    except:
        print("Wrong Input")

users = {'admin':{'balance':0,'password':'admin'}}
print('Welcome to TheAsyncWorld. \npress 1 to login.\npress 2 for registration')
            account_login()
            print(f"Welcome {username},\nAccount Balance: #{users[username]['balance']}\n{dt.today().strftime('%d %b %Y')}")
            print('-'*100)
            print('Choose From the options below\n 1.Withdraw cash\n 2.Deposit Cash\n 3.Make Complaints')
            get_transaction_status = int(input('>> '))
            if get_transaction_status == 1:
                print('How Much do you want to withdraw?')
                withdraw_amount = int(input('Enter Amount to withdraw: '))
                print("press 'y' to confirm and 'n' to abort")
                withdraw_approve = str('[y/n] >> ')
                if withdraw_approve == 'y':

                    if withdraw_amount > users[username]['balance']:
                        print('You have insufficient balance')
                    else:
                        users[username]['balance'] -=withdraw_amount
                        print(f"Take Your cash")
                else:
                    print('Thank you,Try Again')

            elif get_transaction_status == 2:
                print('How much would you like to Deposit')
                deposit_amount = int(input('>> '))
                print("press 'y' to confirm and 'n' to abort")
                deposit_approve = str(input(('[y/n] >> ')))
                if deposit_approve == 'y':
                    users[username]['balance'] +=deposit_amount
                    print(f'you have just deposited {deposit_amount}\n your new account balance: #{users[username]["balance"]}')

            else:
                print('What issue would you like to report')
                user_complaint = str(input('>> '))
                users[username]['user_complaint'] = user_complaint
                print('Thank you for contacting us')
        else:
            print('You have supplied a wrong password')
    else:
        print('Wrong Login details, Please Try Again')

elif get_login_method == 2:
    print('Welcome, Guest\nFill in the form below ')
    username = str(input('Username: '))
    password = str(input("Password: "))
    print('Do you want to submit [y/n]')
    submit_response = input('[y/n]: ')
    if submit_response == 'y':
        users[username]['password']=password
    elif submit_response == 'n':
        print('You can login if you already have an account.\nThank you')
    else:
        print('Please check your input')
else:
    print('Wrong Input')
except ValueError:
print('Wrong Input')