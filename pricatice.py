
class Employee():

    def __init__(self,name):
        self.name=name
        

    def  name_of_employ(self):
        self.Employ=[]
        

    def Hire_employ(self):
        self.Employ.append(self.name)
    

    def show(self):
        for all in self.Employ:
            print("all Employs:",all)



while 1:
    

 objec=Employee(name=input("Enter the name:"))
 objec.name_of_employ()
 objec.Hire_employ()
 objec.show()