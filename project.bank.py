#bank project

balance=int(input("Enter the balance:"))

def chack_balance():
    print(f'$your balance{balance}')

    


def deposit(amount):
    global balance
    balance+=amount
    if(-amount>0):
     
     print(f'${amount}add')
    else:
       print("the sure amount you should add")
    
def withdraw(amount):
   global balance
   balance-=amount
   if(amount>balance):
     print("not enough money")
     
   elif(amount<0):
     print("enter the avalabe amount")
   else:
     balance=balance-amount
     
     
     print("you receive the money=",amount)
      



def bank_operation():
   while True:
    print("\nwelcome to bank")
    print(".1.check the balance")
    print("2. deposite the money")
    print("3. withdraw the money")



    choice=int(input("choice the option"))
    if(choice==1):
       chack_balance()
       
          
   
    elif(choice==2):
       amount=int(input("Enter the money your want add:"))
       deposit(amount)
    elif(choice==3):
       amount=int(input("Enter the amount you want to withdraw;"))
       withdraw(amount)
      










bank_operation()
