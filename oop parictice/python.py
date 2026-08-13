class father:

    def __init__(self,name):
        self.name=name


class mother:


    def __init__(self,last_name):

        self.last_name=last_name


class child(father,mother):

    def __init__(self,family_name,name,last_name):
        self.family_name=family_name
        father.__init__(self,name)
        mother.__init__(self,last_name)


    def display(self):
        return print(f"your name is :{self.name},your last name is :{self.last_name},and Your family name is :{self.family_name}")



obj=child("KING","parveez","Aghan")



print(obj.family_name)

print(obj.name)
print(obj.last_name)

obj.display()