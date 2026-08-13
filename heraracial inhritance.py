# one parent class which Drive multiful child class

class Human:
    def __init__(self,name,last_name):
        print("init for Human class")
        self.name=name
        self.last_name=last_name
    
    def shwo_Human(self):
        print("My name is :{} and my last name is:{}".format(self.name,self.last_name))


class Male(Human):
    def __init__(self,f_name,age,id,name,last_name):
        print("iniit form Male")
        self.f_name=f_name
        self.age=age
        self.id=id
        Human.__init__(self,name,last_name)
    def show_Male(self):
        print("My father name is {} , age is :{} and MY id is :{}".format(self.f_name,self.age,self.id))


class Famle(Human):
    def __init__(self,address,contry,name,last_name):
        print("init form famle")
        self.address=address
        self.contry=contry
        Human.__init__(self,name,last_name)
    
    def show_Famle(self):
        print("My address is:{} and My contry is :{}".format(self.address,self.contry))




#obj=Famle("jalalabad","AFghanistan","parveez","Afghan")
#obj.show_Famle()
#obj.shwo_Human()

obj1=Male("faiz mohammad",21,10,"jamil","khan")
obj1.show_Male()
obj1.shwo_Human()