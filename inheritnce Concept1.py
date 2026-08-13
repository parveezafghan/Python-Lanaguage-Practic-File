'''
oop building block are

1.inheritance 
2. polymorphism
3.Encapsulation
4.Abstraction

inheritance.is the proces of acquiring the properties of one class in another class ,or parent -child
relation is known as inheritnce.
'''


class test1:       #parent
    def __init__(self):
        print("this is test1 constrator")
    

    def method(self):
        print("this is test1 mehtod")
    

    def method1(self,name):
        print("this is method1 of test1 and name is ",name)
    


class test2(test1):            #child
    def __init__(self):
        print("This is test2 constrator ")
    

    def method3(self):
        print("this is test2 method3")
    


    def method4(self,name):
        print("this is test2 mehtod4 and name is ",name)






obj1=test2()
obj1.method3()
obj1.method4("king")
obj1.method()
obj1.method1("parveez")