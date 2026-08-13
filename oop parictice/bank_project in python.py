total_amount=0
withdraw=0
deposite=0


class make_account:

    def __init__(self,name,last_name,f_name,address):
        self.name=name
        self.last_name=last_name
        self.f_name=f_name
        self.address=address
    

    def show_account(self):
        
        print("Welcome Your make account in kabul Bank")
        print("Your name is :{} ,your last name is:{} ,Your father name is:{} and Your address is :{}".format(self.name,self.last_name,self.f_name,self.address))


class deposite():
    def __init__(self,amount):
        self.amount=amount
    

    def show_deposite(self):

        if(self.amount<=0):
            print("add the positive amount:",self.amount)
        else:
         globals()['total_amount']+=self.amount

         print("Your deposite amount is :{}".format(self.amount))


class withdraw():
    def __init__(self,amount1):
        self.amount1=amount1
    

    def show_withraw(self):
        if(self.amount1>globals()['total_amount']):
            print("Your amount is out of range and your curren amount is :%d"%self.amount1)
        else:
         globals()["total_amount"]-=self.amount1
         print("Your withdraw amount is :{}".format(self.amount1))
class check_amount:
    def show_amount(self):
        print("Your total amount is:{}".format(globals()["total_amount"]))

while 1:
 print("1. for make account \n 2.for deposite amount \n for 3.withraw amount\n 4.for check amount")
 select=int(input("Select the operation:"))
 if(select==1):
    object_of_make_account=make_account(name=(input("name")),last_name=(input("last name:")),f_name=(input("f_name:")),address=(input("address:")))
    object_of_make_account.show_account()
 elif(select==2):
     object_deposite=deposite(amount=int(input("Select the amount Your want add:")))
     object_deposite.show_deposite()
 elif(select==3):
     object_widraw=withdraw(amount1=int(input("Select the amount Your widraw :")))
     object_widraw.show_withraw()
 elif(select==4):
     object_check=check_amount()
     object_check.show_amount()
 else:
     print("invilide select:",select)