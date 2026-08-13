# def  __del__(self):
# the __del__() method is known as a destructor method in python
# the __del__() method is called for any object when the reference count for that object becomes zero.
# the reference count of that object become zero when the applicatioan ends or we delete all refrence manually using the del keyword


class mclass(object):
    
    def method(self,name,addres,salary):
        self.name=name
        self.addres=addres
        self.salary=salary
        print("My name is {} My salary is {} and My adddres is {}".format(self.name,self.salary,self.addres))

   
    def method1(self):
        print("Hi this is method1 / ",self.name)
      

   
    def __del__(self):
        print("Hi this is deconstrator function") 


      


obj=mclass()

obj.method('parveez','Nangrahar',10000)

obj.method1()

while True:
    i=int(input("Enter the name"))
    if(i==1 or i==2 or i==3 or i==4):
        
        break
    if(i==5):
        del obj
    
