'''
class amount():
    def __init__(self,studens,amount):
        self.studens=studens
        self.amount=amount
        self.studens=int(input("Enter the studen:"))
        self.amount=int(input("Enter the amount:"))
    
    def show(self):

        self.amount=self.studens*self.amount
        print("total amount;",self.amount)
        print("enter the stude:",self.studens)
       
obj=amount(studens=0,amount=0)
obj.show()
'''
'''
class pass1():
    def __init__(self,pass2):

        self.pass2=pass2
        self.pass2=int(input("Enter passsword:"))
    def show(self):
        return True if(self.pass2==123) else False
    

while True:
 obj=pass1(pass2=0)
 print(obj.show())
 '''
#totla=0
count=0
class loop():
    def __init__(self):
     print("this is constraor")

    def show(self):
        totla=0,
        for self.num in range(1,100,10):
            print(self.num)
            totla+=self.num
            print(totla)
           
            



obj=loop()
print(obj.show())
