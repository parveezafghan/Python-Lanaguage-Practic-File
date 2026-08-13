class parent():

    def __init__(self,name,last_name):
        self.name=name
        self.last_name=last_name
    
    def show_parent(self):

        print(f'My Name is :{self.name} and My last Name is :{self.last_name}')

class child(parent):

    def __init__(self,f_name):

        self.f_name=f_name
    
    def show_child(self):

        print("My father Name is {}".format(self.f_name))

class child1(child):
    tax=0
    def __init__(self,salary,position,Grade):
        self.salary=salary
        self.position=position
        self.Grade=Grade
        
    
    def show_chil1(self):

        if(self.salary>10000):
            self.tax=self.salary*50/100
            print(f"Your salary is:{self.salary} tax is :{self.tax} ")
    
        print(f"Your Grade is {self.position}")
        print(f"YOur Grade is :{self.Grade}")

class child2(child1):
    def __init__(self,address,Age,contry,name,last_name,f_name,salary,position,Grade):
        self.address=address
        self.Age=Age
        self.contry=contry
        parent.__init__(self,name,last_name)
        child.__init__(self,f_name)
        child1.__init__(self,salary,position,Grade)
    
    def show_child2(self):
        print("Your addreess is :{} ,your age is :{} and Your contry is {}".format(self.address,self.Age,self.contry))

child2_ob=child2("jalalabad",21,"Afghanistan","parveez","Afghanistan","Faiz mohammad",12000,1,'A')
child2_ob.show_child2()
child2_ob.show_parent()
child2_ob.show_child()
child2_ob.show_chil1()