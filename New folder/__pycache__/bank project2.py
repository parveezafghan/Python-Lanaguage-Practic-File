#bank project2

balance=int(input("Enter the balance:"))

def check_balance():
    print(f'${balance}')


def deposit(amount):
    global balance
    if(amount>0):
     balance+=amount
    print(f"${amount}")


def withdraw(amount):
    global balance
    #amount=amount-balance
    if(amount>balance):
     ("not enough money in account") 
    elif(amount<0):
     print("not enough money in account")
    else:   
      balance-=amount
      print(f'${amount}')


def bank_operation():
 while True:
    
    print(" welcome to bank:")

    print(".1 check balance:")
    print(".2 deposit:")
    print(".3withdraw:")

    
    
    choice=int(input("choice the option:"))
    if(choice==1):
            check_balance()
    elif(choice==2):
            amount=int(input("select the money:"))
            deposit(amount)
    elif(choice==3):
            amount=int(input("select the money your want:"))
            withdraw(amount)




bank_operation()