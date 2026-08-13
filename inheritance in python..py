class A:

    def __init__(self,name,second_name,f_name):
        self.name=name
        self.second_name=second_name
        self.f_name=f_name

    def method (self):

     print(f"My name is {self.name} and My seocnd name {self.second_name}  and My father name is {self.f_name}")


class B(A):

    def __init__(self,address,city):
        self.address=address
        self.city=city
    
    def method1 (self):
        print("My address is {} and My city is {}".format(self.address,self.city))


class c:
    def __init__(self,experince,expert):
        self.experince=experince
        self.expert=expert
    def method3(self):
        print(f"My experenc is {self.experince} and  i am {self.expert}")


class D(B):
    def __init__(self,salary,id,address,city,name,second_name,f_name):
        self.salary=salary
        self.id=id
        B.__init__(self,address,city)
        A.__init__(self,name,second_name,f_name)
    def method4(self):
        print("My salary is {} and MY id is {} ".format(self.salary,self.id))


obj=D(10000,10,"Afghanistan",'jalalabad',"parveez",'Afghan','faiz mohammad')
obj.method4()
obj.method1()
obj.method( )
print(D.mro())


obj1=c("two yers",'python')
obj1.method3()
