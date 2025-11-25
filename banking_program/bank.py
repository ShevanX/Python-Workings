#bank.py
import vault

def validate(name, acNum):
    return acNum in vault.details and vault.details[acNum]["name"] == name

def check_amount(acNum, amount):
    if amount <= 0:
        return False
    return vault.give_balance(acNum) >= amount

def view_Balance(acNum):
    return vault.give_balance(acNum)



def deposit(acNum, amount):
    balance = vault.give_balance(acNum)
    if not amount <= 0:
        new_amt = balance + amount
        vault.update_balance(acNum, new_amt)
        return vault.give_balance(acNum)
    else:
        return "Invalid Amount"

def withdraw(name, acNum, amount):
    if validate(name, acNum) and check_amount(acNum, amount):
        balance = vault.give_balance(acNum)
        new_balance = balance - amount
        vault.update_balance(acNum, new_balance)
        return vault.give_balance(acNum)
    else:
        return "Withdraw failed."


