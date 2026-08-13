#Banking project in python 
balance=0
def chick(balance):
    balance

def witdraw(balance):
    balance

def deposit(balance):
    balance

while True:
    print("                                                 WELCOME TO THE AFGHAN BANK")
    print("====================================================================================================================================================")
    print("                                                   Service for customer") 
    print("                                               For chicking amount prass (1):")
    print("                                               For withdraw amount prass (2):")
    print("                                               For deposit amount prass (3):")
    print("_____________________________________________________________________________________________________________________________________________________")
    num=int(input("                                             Selec the option"))

    if (num==1):
        chick(balance)
        print("your total amount in your account:",balance)
    elif(num==2):
        witdraw(balance)
        num1=int(input("Enter the amount your want:"))
        if(num1>balance):
            print("your amount is not enough add the amount:",balance)
        else:
            balance=balance-num1
            print("your amount your withdraw:",num1)
    elif(num==3):
        deposit(balance)
        num3=int(input("Enter the amount your want to add :"))
        balance=balance+num3
        print("your amount to add the account:",num3)