# local variables(class variabl ,method variable) and Global variable
#local method variable we can use in the inside  of method
#local class varible we can use in the inside of class some time use (self)key word
# Global variable it can use in evry class in every method/some time .Globals ()['name']
# if we have in same name variable give the priority to method locical variable

'''
name="parveez"
neck_name="Afghan"
class mclass:
    num=100       #class local variable inside of class using
    num1=400
    def method(self):
        x=50          # local variable using inside of mehtod
        y=50
        print("this is local method vairble :",x+y)      # local varible using inside of methodd
        print("this is class local viarble inside the class  :",self.num*self.num1)
        print("my name is ",name,"and neck name is ",neck_name)

    def method1(self,x,y):
        print("this is local method variale :",x+y)
        print('this is local class variale inside of class :',self.num+self.num1) # local class variable 
        print("my name is ",name,"and my neck name is ",neck_name) # Globa variable








        

obj=mclass()
obj.method()
obj.method1(50,50)


class mclass2:
    def method3(self):
        print("Global varible in class2 and method3 ",name,neck_name)



obj1=mclass2()
obj1 .method3()
'''
'''
name='parveez'
id=1890

class mclass(object):
    name='mobeen'
    id=123
    def method(self):
        print("my name is ",self.name,'and my id is',self.id)
    
    def methodd2(self,name,id):
        print("my name is ",name,'and my id is',id)
        print("my name is ",globals()['name'],globals()['id'])





obj=mclass()
obj.method()
obj.methodd2('jamil',12345)
'''


'''
name='parveez afghan'
id=123



class nameclass(object):
    age=21
    salary1=300000
    def method(self):
        print("my salary is ",self.salary1,'and my is ',self.age,'years old')



    
class msclass():
    def method1(self):
        print('MY  name',globals()['name'],'and my id number ',globals()['id'],"")





obj=nameclass()
obj.method()

obj1=msclass()
obj1.method1()
'''


'''
num=int(input('Enter the number:'))
num1=int(input("Enter the number:"))


class math():
    def adition(self):
        print("Total adition of numbers:",globals()['num']+globals()['num1'])




obj=math()

obj.adition()
'''


id=100
salary=30000
name='parveez afghan'

class mclass:
    
    def method(self):
        living_place='hada'
        print("my living palce is",living_place)
        self.living_place=living_place
    
    def method1(self):
        print("my id is ",globals()["id"])
        print("my salary is ",globals()["salary"])
        print("my name is ",globals()["name"])
    
    def method2(self):
        print("my addres is ",self.living_place)
    




obj=mclass()
obj.method()
obj.method1()
obj.method2()



