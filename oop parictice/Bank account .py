# first example
'''
class Bank_account1:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    
    def depsite(self,amount):
        self.amount=amount
        self.balance+=amount

    def wirdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
        
        else:
            print("Insuficince found")
    def get_balance(self):
        return self.balance
    

    def account_inf(self):
        return f"account holder{self.account_holder},balnce{self.balance}"
    
account=Bank_account1("bob",10000)

account.depsite(10000)
print(account.get_balance())

print(account.account_inf())
'''
                                   # second example 
'''
while True:
 name=input("Entr the name:")
 mm=int(input("enter the balance:"))
 class Band_account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance

    

    def deposit(self,amount):
        self.balance=self.balance+amount
        self.amount=amount

    def get(self):
       return self.balance


 obj=Band_account(globals()['name'],100000)
 obj.deposit(globals()['mm'])
 print(obj.get())
'''
                                              #third example
'''
class Employee:
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position
    
    def promot(self,new_positon):
        self.position=new_positon
    
    def increase_salary(self,amount):
        self.salary+=amount
    
    def employee_inf(self):
        return f"name{self.name} you salary{self.salary} your position {self.position}"
    


    def longe_salary(self):
        return self.salary 
    

obj=Employee('parveez',1000,"developer")

obj.increase_salary(100)

print(obj.employee_inf())

print(obj.longe_salary())
'''
#                                              forth example
'''
name1=input("Enter your name:")
salary1=int(input("Enter your salary:"))
position1=input("Enter your position:")
amount1=int(input("Enter the amount:"))
class Employee(object):
    def __init__(self,name,salary,position):
        self.name=name
        self.salary=salary
        self.position=position

    
    def promot(self,amount):
        self.salary+=amount


    
    def result(self):
        return self.salary
    


    def infromation(self):
        return f"my nmae is {self.name} my salary is {self.salary} my position is {self.position}"
    



obj=Employee(globals()['name1'],globals()['salary1'],globals()["position1"])
obj.promot(globals()['amount1'])

print(obj.infromation())
 '''
  '''                                                          #fivth example 
while True:
 city1=input("Enter the name of city:")
 tempereture1=int(input("Enter the tempreture:"))
 condition1=input("Enter the conditon of city :")
 class weater:
    def __init__(self,city,tempereture,conditon):

        self.city=city
        self.tempereture=tempereture
        self.conditon=conditon

    def update_tem(self,new_tem):
        self.tempereture=new_tem

    
    def update_tem(self,new_condition):
        self.conditon=new_condition
    

    def get_weather(self):
     return   f'city{self.city} tempretur{self.tempereture} condtion {self.conditon}'



 obj=weater(globals()['city1'],globals()['tempereture1'],globals()['condition1'])

    
 print(obj.get_weather())

'''






        
