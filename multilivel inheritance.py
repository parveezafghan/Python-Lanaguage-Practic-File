class parent:
    def __init__(self,name,f_name):
        self.name=name
        self.f_name=f_name
    
    def show_parent(self):
        print("My name is :{} and My father name is :{}".format(self.name,self.f_name))
    
class child(parent):
    def __init__(self,university,semester):
        self.university=university
        self.semester=semester
    
    def show_child(self):
        print(f"I am in :{self.university} and My semester is {self.semester}")



class child1(child):

    def __init__(self,addres,pess):
        self.addres=addres
        self.pess=pess
    
    def show_child1(self):
        print("i am living in the :{} and My To tall semester pee is:{}".format(self.addres,self.pess))

class child2(child1):
    def __init__(self,contry,provienc):
        self.contry=contry
        self.provience=provienc
    
    def show_child2(self):
        print("MY contry name is :{} and My provience name is :{}".format(self.contry,self.provience))


class child3(child2):

    def __init__(self,salary,position):
            self.salary=salary
            self.position=position
        
    def show_child3(self):
        print(f"MY slary is :{self.salary} and MY position is :{self.position} ")


class child4(child3):
    def __init__(self,id,Grade,name,f_name,university,semester,addres,pess,contry,provienc,salary,position):
        self.id=id
        self.Grade=Grade
        parent.__init__(self,name,f_name)
        child.__init__(self,university,semester)
        child1.__init__(self,addres,pess)
        child2.__init__(self,contry,provienc)
        child3.__init__(self,salary,position)

    

    def show_child4(self):
        print("My id is:{} and My Grade is :{}".format(self.id,self.Grade))

class show_all(child4):
    def show_all1(self):
     #   parent.show_parent()
       child.show_child(self)
    
       child1.show_child1(self)
       
       child2.show_child2(self)

       child3.show_child3(self)

       child4.show_child4(self)

       parent.show_parent(self)
       

oject_child4=child4(10,"A","parveez",'Faiz mohammad',"Alpala","first","Jalalabad",21000,'Afghanistan',"jalalabad",100000,1)
oject_child4.show_child4()
oject_child4.show_parent()
oject_child4.show_child()
oject_child4.show_child1()
oject_child4.show_child2()
oject_child4.show_child3()
ojecct5=show_all(10,"A","parveez",'Faiz mohammad',"Alpala","first","Jalalabad",21000,'Afghanistan',"jalalabad",100000,1)
ojecct5.show_all1()

