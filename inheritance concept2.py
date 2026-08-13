
num1,num2=1000,9000              # Globals variable
class parent:
    x,y=100,400                  # paret  class variable 


class child(parent):
    z,x=900,100                  # child class variable


    def add(self,a,b):            # method local variable
        print(a+b)                # access method variable

        print(globals()['num1']+globals()['num2']) # access Globals variable

        print(super().x+super().y) # access parents class variable 

        print(self.z+self.x)        # access class variable







obj=child()
obj.add(10,20)

'''

'''

x,y=500,500
class parent:
    x,y=100,200
    def add(self):
        self.x=x
        self.y=y
        return x+y
    

    def method(self):
        x,y=900,100
        return x*y
    
    def method1(self):
        return globals()['x']+globals()['y']
    



class child(parent):
    def method4(self,x,y):
     
     return x*y
    

    def method5(self):
        return super().x+super().y
    

    def method6(self):
        return globals()['x']+globals()['y']
obj=child()
print(obj.method1())
print(obj.method())
print(obj.method4(100,400))
print(obj.add())

print("this uper :",obj.method5())

print("Globals :",obj.method6())

'''

'''
age=10
salary=100000
class mclass:
    name='parveez'
    second_name='Afghan'
    reslary=0
    
    def method(self):
        return (self.name,self.second_name)
    
    def information1(self,):
        return globals()["age"],globals()['salary']
    
    def method5(self,salary):
        if salary>10000 and salary==500:
            self.reslary=salary-100
            return salary
        
        print(salary)
        
    print(reslary)
        
    
    

class mmclass(mclass):

    def __init__(self,age,salary):
        print("age",age,"salary",salary)

    def infomation(self,name,second_name):
        return name,second_name
    
    def method3(self):
        return super().name , super().second_name
    






obj=mmclass(19,300000)
print(obj.infomation("amanullah",'mobeen'))

print(obj.method3())

print(obj.method5(11000))
    




class mclass():
    id=121
    salary=1000
    Full_name="parveez Afghan"
    def __init__(self):
        print("MY id is :",self.id)
        print("My salary is :",self.salary)
        print("MY full name is :",self.Full_name)
    

    def method(self,address,city):
        self.address=address
        self.city=city
        print("MY address is :",self.address)
        print("MY living town:",self.city)


class mclass1(mclass):
    id=100
    salary=2000
    Full_name="amanulah mobeen"
    def __init__(self):
        print("My id is :",self.id)
        print("My salary is :",self.salary.uper())
    
























obj=mclass1()


print(obj.method("hada","jalalabad"))
