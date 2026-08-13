class Human:

    def __init__(self,name,second_name,last_name):
        self.name=name
        self.second_name=second_name
        self.last_name=last_name
        return print("My name is :{} My second name is :{}  My last name is :{}".format(self.name,self.second_name,self.last_name))



class Male(Human):

    def __init__(self,salary,id,Grade,name,second_name,last_name):
        self.salary=salary
        self.id=id
        self.Grade=Grade
        Human.__init__(self,name,second_name,last_name)
        return print("My monthly salary:{}: My id is :{}: My Grade is :{}".format(self.salary,self.id,self.Grade))

obj2=Male(100,10,"A",'jamil','awan','Rashid')
class famle(Human):

    def __init__(self,corrent_address,city):
        self.corrent_address=corrent_address
        self.city=city

        return print("corrent address{}: my city is:{}".format(self.corrent_address,self.city))


class experience(Human):
    def __init__(self,experience,expert,name,second_name,last_name):

        self.experience=experience
        self.expert=expert
        Human.__init__(self,name,second_name,last_name)
        return print("i have {} month experience: and i am expert is {}".format(self.experience,self.expert))


obj=experience(2,"python",'parveez',"Afghan",'king')

obj=famle("Afghanistan",'jalalabad')