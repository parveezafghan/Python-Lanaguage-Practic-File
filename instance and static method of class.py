# istance & static methods of class
# istance method are those mehtod whch need for calling classe objec and we cant call without class object
# if we have static method don,t for (self)keyword/and static method don,t need for calling direct object and we call direct class
# for static method we use /    @staticmethod



class mclass:
    id=1223
    salary=10000
    def method(self):
        print("my id is ",self.id,'my salary is ',self.salary)
    


    @staticmethod
    def method1(name,adress):
        print("my name is:",name,"my adress is",adress)
    

    
    def mehtod2(self):
        Grade="A"
        position=1
        print("my Grad is",Grade,"my position is",position)
    

    
    def method3(self):
        tax=1000
        self.tax=tax
        
        print("your tax",tax)
        
    def tax1 (self):
        self.tax=self.salary-self.tax

        print("your tax in salary:",self.tax)



obj=mclass()
obj.method()
mclass().method1('parveez afghan','Nangrahar')
obj.mehtod2()
obj.method3()
obj.tax1()

        
