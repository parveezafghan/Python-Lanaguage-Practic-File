

balance=0
amount=0

def chick(balance):
    

    print(f"&{balance}")

def withdraw(amount):
    amount=int(input("Enter the amont your want to withdraw:"))
    global balance
    if(amount<balance):
        print(f"you amoun is not enough{balance}")
    else:
        balance-=amount
        
        print(f"your withraw amount{amount}")

def deposit(amoun):
    amoun=int(input("Enter the amount to add in account:"))

    global balance

    balance-=amoun
    print(f"Your are deposite amount {amoun}")


while True:
    
    print("                                                WELCOME TO AFGHAN BANK")
    print("------------------------------------------------------------------------------------------------------")
    print("                                                   Selec the operation")
    print("                                                   1. chicking amount")
    print("                                                   2.withdraw amount")
    print("                                                   3. deposite amount") 
    print("________________________________________________________________________________________________________")
    num=int(input("                                                      Selec the operation:"))
    if(num==1):
        chick(balance)
        print(f"Your total amount{balance}")
    elif(num==2):
        
        withdraw(amount)
        
    elif(num==3):
        deposit(amount)

