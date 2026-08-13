'''

gender=input("your gender(m,f):")
id=input("your id(yes,no):")
pass1=input("your pass(yes,no):")
ticket=input("your ticket(yes,no):")



if(gender=='male',print("male")):
     
    if(id=='yes'):
        if(pass1=='yes'):
            if(ticket=='yes'):
                print("your can go")
            else:
                print("you don,t have ticket")
        else:
            print("you don,t have passport")
    else:
        print("you don,t have id_card")           
else:
    print("invilid gender")
'''


#Bank system

'''
blance=int(input("ente the mony"))

def check_balance():
    print(f"your blance:${'balance'}")


def deposit(amount):
    global check_balance
    if amount>0:
        balance+=amount
        print(f'${"amount"}add')
    else:
        print("enter the sure credit")

def withdraw(amount):
    global balance    
    if amount>balance:
        print("not enough money")
    elif(amount<0):
        print("enter the mony")
    else:
        balance-=amount
        print(f'${'amount'}wowatale')
    
def bank_operation():
    while True:
        print("welcome to the bank")
        print(".1.exist balance")
        print(".2.add the money")
        print(".3.loos money")
        print(".4.loss")
        
        choice=input("selet the choice:")
        if(choice=="1"):
            check_balance
        elif(choice=="2"):

            amount=float(input("add the money "))
            deposit((amount))
        elif(choice=="3"):
            amount=float(input("retrive money "))

            withdraw(amount)
        elif(choice=='4'):
            print("think you")
            break
        else:
            print("invilide choice")

'''


balance=int(input("enter the balance"))

def check_balance():
    print("your balance")

def deposit(amount):
    global balance
    if(amount>0):
        balance+amount

        print("your add money",balance)
    else:
        print("enter the money")
    
def widthraw(amount):
    global balance
    if amount> balance:
        print("not enough money")
    elif amount<=0:
        print("enterr sure money")
    else:
        balance-=amount
        print("mony loss")
    

def operation():
    while True:
        print("welcome to bank")
        print("1.exict mony")
        print(".2 deposite")
        print("3.widtraw")
        print(".4.watal")
        choice=input("choice the option:")
        if(choice==1):
            check_balance()
        elif(choice==2):
            amount=float(input("enter mony "))
            deposit(amount)
        elif(choice==3):
            amount=float(input("selet the mony you  want :"))
            widthraw(amount)
        elif(choice==4):
            print("think you ")
            break
        else:
            print("invlide seclection")


operation()
        

    
    
   
