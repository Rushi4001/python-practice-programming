
import threading
amount=1000

def atm(func):
    func()


def deposite():
    value=int(input("enter amount to deposite"))
    global amount
    amount=amount+value
    print("deposite succesfull-balence:",amount)


def withdraw():
    value=int(input("enter amount withdraw"))
    global amount
    if value>amount:
        print("there is no sufficience balence")
    else:
        amount=amount-value
        print("withdraw succesfull-balence:",amount)

def main():
    print("inside main")
    atm(deposite)
    atm(withdraw)








if __name__=="__main__":
    main()