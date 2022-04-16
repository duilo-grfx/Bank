"""
Abduljabbar Said
Bank
"""

class Account:
    def __init__(self, user, pin, amount):
        self.user = user
        self.pin = pin
        self.amount = amount

    def get_user(self):
        return self.user

    def get_pin(self):
        return self.pin

    def get_amount(self):
        return self.amount
    # self.amount=how much they have in account
    # set.amount changes the money in their account


    def set_amount(self, newBal):
        self.amount = newBal
        return self.amount

# (user, pin, balance)
accounts = {"snasr": Account("snasr", 8888, 5600),
            "ytour": Account("ytour", 4242, 8500),
            "vkomp": Account("vkomp", 4444, 12500)}

accounts["snasr"] = Account("snasr", 8888, 5600)
accounts["ytour"] = Account("ytour", 4242, 8500)
accounts["vkomp"] = Account("vkomp", 4444, 12500)


def main():
    try:
        print("This program will help you find out your account balance\
once you sign in and hav a valid login")
        ID = input("please enter your id: ")
        Pin = int(input("Please enter your pin: "))
        # see if both matches in the dictionary
        if ID in accounts and Pin == accounts[ID].get_pin():
            a = accounts[ID]
            print("Welcome to your account")
            print("Your current balance is: ", "$", a.get_amount())
        else:
            print("Please try again")
        # making dummy accouts
        my_atm = ATM(a)
        my_atm.transact()
    except:
        print("Not valid")


class ATM:

    def __init__(self, account):
        self.account = account

    def transact(self):
        DpWd = input("Would you like to deposit or withdraw? ")
        mon = input("How much money? ")

        if DpWd == "deposit":
            # adding the balance with the deposited amount
            dep = self.account.set_amount(self.account.get_amount() + int(mon))
            print("Your new balance is", (dep))
        elif DpWd == "withdraw":
            # subtract the balance with the deposited amount
            wit = self.account.set_amount(self.account.get_amount() - int(mon))
            print("Your new balance is", (wit))
        else:
            print("Not an option")
