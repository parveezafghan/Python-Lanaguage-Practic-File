 # conversion of local method vairble if we have local method vairble to change to class varible we shoult use
# if we have salar.converto class vairble /self.salar=salary



'''
class test:
    Tax=10
    def method(self,name,salar):
        print("My name is ",name,)
        print("My salary is ",salar)
        self.salary=salar
        self.name=name

    

    def showTax(self):
        print("salary-tax=",self.salary-self.Tax)

    

    def showallinoneline(self):
        print("name",self.name,'salary',self.salary,'tax',self.Tax,'payble',self.salary-self.Tax)


    

obj=test()
obj.method("parveez",10000)
obj.showTax() 

obj.showallinoneline()
'''

'''
class math:
    def get_Data(self,num1,num2):
     num=int(input("selec the choice(1.add)(1.mult)(3.sub)(4.divison):"))
     num1=int(input("Enter the first number:"))
     num2=int(input("Enter the seond number:"))
     self.num=num
     self.num1=num1
     self.num2=num2

     if(num==1):
        self.add()
     elif(num==2):
        self.mult()
     elif(num==3):
        self.sub()
     elif(num==4):
        self.division()




    

    def add(self):
       print("adition of two number:",self.num1+self.num2)
       
    


    def mult(self):
       print("multiflication of two numbers:",self.num1*self.num2)
    

    def sub(self):
       print("Total substration:",self.num1-self.num2)
    

    def division(self):
       print("Your Total division:",self.num1/self.num2)



    

math().get_Data(num1=0,num2=0)
'''




class mclass:
    tax=1000
    def method(self):
        name='parveez '
        secon_name="Afghan"
        print("my name is",name)
        print("my secon name is ",secon_name)
        self.name=name
        self.secon_name=secon_name

    def method1(self,position,Grade):
        print("My position is ",position)
        print("My Grade is",Grade)
        self.position=position
        self.Grade=Grade

    def  method2(self):
        id=199
        salary=10000
        print("my id",id)
        print("my salary is",salary)
        self.id=id
        self.salary=salary
        
    def show_all(self):
        print('my name is ',self.name,'and my second name is',self.secon_name,"my position",self.position,'my Grade',self.Grade,'my id is',self.id,"my salary is",self.salary,"payable tax is",self.salary-self.tax)





obj=mclass()
obj.method()
obj.method1(1,"A")
obj.method2()
obj.show_all()