
class father:
    def __init__(self,name):
        self.name=name
    
    def work(self):
        print("I can Do this work")



class mother:
    def __init__(self,last_name):
        self.last_name=last_name
    def work(self):
        print("I can,t Do this work")


class child(father,mother):
    def __init__(self,family_name,name,last_name):
        print("My faily name is:",family_name)
        self.family_name=family_name

        father.__init__(self,name)
        print("my name is :",name)
        mother.__init__(self,last_name)
        print("My last name is:",last_name)
    def work(self):
        print("I have done this work")

    def display_My_info(self):
        return print(f"My name is:{self.name} ,My last name is :{self.last_name} and My family name is:{self.family_name}")

obj=child("ahmad zy","parveez","Afghan")
obj.display_My_info()

