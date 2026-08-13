#more then one parent class is called multifull inheritance in python


class name1(object):
    def __init__(self,name,second_name,f_name):
        self.name=name
        self.second_name=second_name
        self.f_name=f_name
    

    def show(self):
        print(f"my name is {self.name} , my second name is {self.second_name} and My father name is {self.f_name}")


class information():
    def __init__(self,birth_date,age,):
        self.birth_date=birth_date
        self.age=age
    

    def show(self):
        print("my birth date is :{} and i am  :{} years old".format(self.birth_date,self.age))


class family():

    def __init__(self,all_family_mambers,Your_brothers,Your_sisters,):
        self.all_family_mambers=all_family_mambers
        self.Your_brother=Your_brothers
        self.Your_sister=Your_sisters

    
    def show(self):
        print("your all family mumber is :{} ,i have :{} brothers and i have :{} sisters".format(self.all_family_mambers,self.Your_brother,self.Your_sister))

class location():
    def __init__(self,contry,city,destric):
        self.contry=contry
        self.city=city
        self.destric=destric
    

    def show(self):
        print(f" MY contry name is :{self.contry},MY city is :{self.city},and MY destric is :{self.destric}")

class expert(name1,information,family):
    def __init__(self,experience,expert,name,second_name,f_name,birth_date,age,all_family_mambers,Your_brothers,Your_sisters,contry,city,destric):
        self.experience=experience
        self.expert=expert
        name1.__init__(self,name,second_name,f_name)
        information.__init__(self,birth_date,age)
        family.__init__(self,all_family_mambers,Your_brothers,Your_sisters)
        location.__init__(self,contry,city,destric)
    def show(self):
        print(f"i am expert in {self.expert} and my experience is :{self.experience} months")

obj=expert(2,"python","parveez","Afghan","Faiz mohammad",[2003,3,3],21,11,7,2,"Afghanistan",'jalalabid','behsod')
obj.show()
name1.show(obj)
information.show(obj)
family.show(obj)
location.show(obj)