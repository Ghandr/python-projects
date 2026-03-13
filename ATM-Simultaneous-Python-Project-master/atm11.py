#!/usr/bin/python
import getpass #الباسورد مش بيظهر ل المستخدم ع الشاشه


# Lists of users, their PINs and balances
users = ['user', 'user2', 'user3']
pins = ['1234', '2222', '3333']
amounts = [1000, 2000, 3000]

# طلب اسم المستخدم
while True:
    user = input('\nENTER USER NAME: ').lower()
    if user in users:
        n = users.index(user)  # جاب رقم اليوزر مباشرة
        break
    else:
        print('----------------')
        print('****************')
        print('INVALID USERNAME')
        print('****************')
        print('----------------')

# التحقق من الـ PIN
count = 0
while count < 3:   #بيسمح له ب  3 محاولات لادخال الباسورد
    pin = str(getpass.getpass('PLEASE ENTER PIN: '))
    if pin.isdigit():
        if pin == pins[n]:
            break
        else:
            count += 1
            print('-----------')
            print('***********')
            print('INVALID PIN')
            print('***********')
            print('-----------\n')
    else:
        print('------------------------')
        print('************************')
        print('PIN CONSISTS OF 4 DIGITS')
        print('************************')
        print('------------------------')
        count += 1

if count == 3:
    print('-----------------------------------')
    print('***********************************')
    print('3 UNSUCCESFUL PIN ATTEMPTS, EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('***********************************')
    print('-----------------------------------')
    exit()

print('-------------------------')
print('*************************')
print('LOGIN SUCCESFUL, CONTINUE')
print('*************************')
print('-------------------------\n')
print('**************************')
print(str.capitalize(users[n]), 'welcome to ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main menu
while True:
    print('-------------------------------')
    print('*******************************')
    response = input(
        'SELECT FROM FOLLOWING OPTIONS: \n'
        'Statement__(S) \n'   #استعلام
        'Withdraw___(W) \n'   #سحب
        'Lodgement__(L)  \n'  #ايداع
        'Change PIN_(P)  \n'  #تغير الباسورد
        'Quit_______(Q) \n: ' #خروج
    ).lower()
    print('*******************************')
    print('-------------------------------')

    if response == 's':  #استعلام
        print('---------------------------------------------')
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE', amounts[n], 'EURO ON YOUR ACCOUNT.')
        print('*********************************************')
        print('---------------------------------------------')

    elif response == 'w': #سحب
        cash_out = int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: '))
        #شرط ان المبلغ يكون من فئات 10 يورو (يقبل القسمه ع10)
        if cash_out % 10 != 0:
            print('------------------------------------------------------')
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10 EURO NOTES')
            print('******************************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('-----------------------------')
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
            print('-----------------------------')
        else:
            amounts[n] -= cash_out
            print('-----------------------------------')
            print('***********************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'EURO')
            print('***********************************')
            print('-----------------------------------')

    elif response == 'l':  #ايداع
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        if cash_in % 10 != 0:
            print('----------------------------------------------------')
            print('****************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 10 EURO NOTES')
            print('****************************************************')
            print('----------------------------------------------------')
        else:
            amounts[n] += cash_in
            print('----------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'EURO')
            print('****************************************')
            print('----------------------------------------')

    elif response == 'p': #تغير الباسورد 
        new_pin = str(getpass.getpass('ENTER A NEW PIN: '))
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            new_ppin = str(getpass.getpass('CONFIRM NEW PIN: '))
            if new_ppin != new_pin:
                print('------------')
                print('************')
                print('PIN MISMATCH')
                print('************')
                print('------------')
            else:
                pins[n] = new_pin
                print('NEW PIN SAVED')
        else:
            print('-------------------------------------')
            print('*************************************')
            print('NEW PIN MUST CONSIST OF 4 DIGITS \nAND BE DIFFERENT FROM PREVIOUS PIN')
            print('*************************************')
            print('-------------------------------------')

    elif response == 'q': #خروج
        print("Thank you for using the ATM. Goodbye!")
        exit()

    else:
        print('------------------')
        print('******************')
        print('RESPONSE NOT VALID')
        print('******************')
        print('------------------')
        