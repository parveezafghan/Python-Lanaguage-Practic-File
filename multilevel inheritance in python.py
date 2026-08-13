

class calculator:
    pass


class sum:
    total=0
    def __init__(self,num,num1):
        self.num=num
        self.num1=num1

    
    def sum(self):
       # self.total=self.total
        self.total=self.num+self.num1

        print("your total adition is :%d"%self.total)

class sub:
    total=0
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    
    def sub(self):
        self.total=self.num1-self.num2

        print("Your total substration:%d"%self.total)
class mul():
    total=0
    def __init__(self,num1,num):
        self.num1=num1
        self.num=num

    def mul(self):

       self.total=self.num*self.num1

       print("your total multiflication:%d"%self.total)

class div():
    total=0
    def __init__(self,num1,num):
        self.num1=num1
        self.num=num
    
    def div(self):
        self.total=self.num/self.num1

        print("Your total divison:%d",self.total)
while 1:

    print("calculator 1.for add 2. for sub 3.mul.  4.div")
    num=int(input("select the operation:"))

    if(num==1):
        obj=sum(num=int(input("Enter the number1:")),num1=int(input("Enter the number 2:")))
        obj.sum()
    elif(num==2):
        obj2=sub(num=int(input("Enter the number 1:")),num1=int(input("Enter the number 2:")))
        obj2.sub()
    elif(num==3):
        obj3=mul(num=int(input("Enter the number 1:")),num1=int(input("Enter the number 2:")))
        obj3.mul()
    elif(num==4):
        obj4=div(num=int(input("Ente the number 1:")),num1=int(input("Enter the number 2:")))
        obj4.div()

