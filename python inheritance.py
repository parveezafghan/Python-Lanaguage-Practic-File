class Humana:

    def __init__(self,name,second_name,last_name):

        self.name=name
        self.second_name=second_name
        self.last_name=last_name

    def show(self):
        return  print(f"My name is :{self.name},:My second name is:{self.second_name}:My last name is :{self.last_name}")
    



class male(Humana):
    def __init__(self,salary,id,Grade):

        self.salary=salary
        self.id=id
        self.Grade=Grade
    
    def show1(self):
        return print(f"my salary is :{self.salary}: and my id is :{self.id}:my Grade is{self.Grade}")
obj3=male(10000,10,"A")
obj3.show1()   
    

class female(Humana):
    def __init__(self,address,name,second_name,last_name):

       self.address=address
       Humana.__init__(self,name,second_name,last_name)

    def show3(self):
        return print("my address is {}".format(self.address))
obj2=female("jalalabad","amanullah",'mobeen','khaksar')
obj2.show3()
obj2.show()


class experience(Humana):
    def __init__(self,experience,expert,name,second_name,last_name):
        self.experience=experience
        self.expert=expert
        Humana.__init__(self,name,second_name,last_name)

    def show4(self):
        return print("My experence is {} months and  i am expert{}".format(self.experience,self.expert))
    



obj=experience(2,"python","Parveez","Afghan",'king')
obj.show4()
obj.show()
print("-----------------------------------------")

obj5=Humana("jamil",'auan','rashad')
obj5.show()
