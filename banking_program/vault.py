#vault.py
import random as r

details = {}

def check_acc(acNum):
    if acNum not in details:
        return False
    else:
        return True


def give_balance(acNum):
    balance = details[acNum]["balance"]
    return balance

def update_balance(acNum, newNum):
    details[acNum]["balance"] = newNum


def new_acc(name, bal):
    while True:
        acc_num = str(r.randint(10000, 99999))
        if acc_num not in details:
            pass
            break

    new_data = {acc_num : {"name" : name, "balance" : bal}}
    details.update(new_data)
    return acc_num



