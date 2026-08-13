
class Humane:

    def __init__(self,name):
        self.name=name
        print("this is the constrator of Human class :",name)

class Male(Humane):

    def __init__(self,last_name):
        self.last_name=last_name

        print("this is the constrator of male class :",last_name)

class famle(Male):

    def __init__(self,family_name,name,last_name):
        self.family_name=family_name

        print("this is the constrator of famle class:",family_name)
        Humane.__init__(self,name)
        Male.__init__(self,last_name)
obj=famle("paktwal","parveez","Afghan")
class programmer(famle):
    def __init__(self,language):
        self.language=language
        print("this is the constrartor of programmer class:",language)

    def display(self):

        return print(f"My name is :",self.name,"My last name is:",self.last_name,"my family name is :",self.family_name,' i learn  language online', self.language)
obj1=programmer("python")
obj1.display()

