'''
Write a python program to withdraw money from bank

Requirements:
    • Balance in bank should not be less than 1000
    • User account will be blocked for an hour if
      user put 3 times wrong pin.
'''
import time


class BalanceExceptionError(Exception):
    pass


class AttemptExceptionError(Exception):
    pass


attempts = 1


def withdraw():
    global attempts
    saved_pin = 1234    # hard-coded bcz no db is connection
    balance = 10000     # hard-coded
    pin = int(input("Enter the pin: "))
    if pin == saved_pin:
        try:
            amt = float(input("Enter amount to withdraw:"))
            temp_bal = balance - amt
            if temp_bal < 1000:
                raise BalanceExceptionError("Insufficient Balance")
            balance = balance - amt
            print("Remained balance is: ", balance)
        except Exception as var:
            print(var)
    else:
        ans = input("Wrong pin. Do you want to continue again:(y/n):")
        if ans.lower() == 'y':
            attempts += 1
            try:
                if attempts == 4:
                    raise AttemptExceptionError("Too many attempts.Blocked AC")
            except Exception as var:
                print(var)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print("Thank you!")
            return


withdraw()
