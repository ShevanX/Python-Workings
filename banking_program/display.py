import bank
import vault

def main():
    print("-----Welcome to the GoldMan Bank-----\n")
    print("How can we help today:")

    while True:
        print("1. View Balance\n2. Deposit\n3. Withdraw\n4. Make a new Account\n5. Exit\n")
        choice = int(input("Pick an Option: "))
        match (choice):
            case 1:
                name = input("What is your name: ")
                num = input("What is your account number: ")
                if bank.validate(name, num):
                    print(f"Your account balance is ${bank.view_Balance(num)}\n")
                else:
                    print("Inalid account details")
            case 2:
                num = input("What is your account number: ")
                amt = float(input("How much do you want to deposit: "))
                bank.deposit(num, amt)
                print(f"${amt} is deposited to your account. Your new balance is {bank.view_Balance(num)}\n")
            case 3:
                name = input("What is your name: ")
                num = input("What is your account number: ")
                amt = float(input("How much do you want to withdraw: "))
                bank.withdraw(name, num, amt)
                print(f"${amt} is withdrawed from your account. Your new balance is {bank.view_Balance(num)}\n")
            case 4:
                name = input("What is your name: ")
                amt = float(input("Whats yoru initial deposit amount: : "))
                new_num = vault.new_acc(name, amt)
                print(f"Your new account is made. Your new account number is {new_num}\n")
            case 5:
                print("Thank you for visiting us. See you later. Bye\n")
                break



if __name__ == '__main__':
    main()
