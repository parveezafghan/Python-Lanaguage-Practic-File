"""
Type of inhritance
1.single level( child , Father)
2.Multi level (child ,Father,grand father)
3. muliple (mother,father,child)
4.hierarchal(father,child,child)
5. Hybrid (multiple+hierarchal)
"""
  

'''
class Box:
    width,height=0,0



class Towd(Box):
    color="Red"
    def __init__(self,width,height,color):
        self.width=width
        self.height=height
        self.color=color
    

    def display(self): 
        print("BOX width",self.width)
        print("Bow height",self.height)
        print("Box color",self.color)
        print("Box total ",self.width*self.height)





class Treed(Towd):
    zAxis=0
    

    def __init__(self,w,h,z):
        self.width=w
        self.height=h
        self.zAxis=z
    

    def display1(self):
        print("Box with",self.width)
        print("Box height ",self.height)
        print("BOx color ",self.color)
        print("Bor area ",self.width*self.height*self.zAxis)

    def chingecolor(self,color):
        self.color=color









    









area=Towd(10,20,"orange")
area.display()
    
print("_________________________________")
obj=Treed(10,20,30)
obj.chingecolor("Blue")

obj.display1()

'''





class Bank:
    amount=int(input("Enter the amount :"))
    def __init__(self,amount):
        amount

    
    def deposit1(self,amount1):
        self.amount+=amount1
      #  print(self.amount)
    


    def widraw(self,amount2):
        self.amount-=amount2
      #  print(self.amount)
        
    

    def display(self):
        print("this is amount %d"%self.amount)

    




obj=Bank(amount=0)


print(obj.display())

