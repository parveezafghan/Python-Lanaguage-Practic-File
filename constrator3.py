# three technic to print data for function 
# stange function( def __str__( self)  ) this method is use when you want to do an operation while printing object of a class .
# it only return a string
''''
class test:
    def __init__(self,name,salary,addres):
        self.name=name
        self.salary=salary
        self.addres=addres
    

    def display(self):
        print("name{} Your salary {} Your address{}".format(self.name,self.salary,self.addres))

    


    def display1(self):
        print("Your name %s Your salary is %g  and Your are address is %s"%(self.name,self.salary,self.addres))


    
    def display2(self):
        print("My name is ",self.name,'My salary is ',self.salary,'and my address is ',self.addres)

obj=test("parveez",10000,"Nangrahar")

obj.display()
obj.display1()
obj.display2()



class test1:
    def __str__(self):
        return "Hi this is string function "
    



obj=test1()

print(obj)
'''


class constrator:
    def __init__(self,name,salary,address):
        self.name=name
        self.salary=salary
        self.address=address
    

    def display(self):
        print("Your name is {} Your salary is {} and Your address is {}".format(self.name,self.salary,self.address))


    def display1(self):
        print("Your name is %s  Your salary is %d  and Your %s"% (self.name,self.salary,self.address))

    def display2(self):
        print("Your name is",self.name,'Your salary is  ',self.salary,'and Your address is ',self.address)
    
    def __str__(self):
        return "this is string function which is calling by object"


obj=constrator("parveez",10000,"Nangrahar")

obj.display()
obj.display1()
obj.display2()
print(obj)