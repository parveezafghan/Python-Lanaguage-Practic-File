

class Attend_in_university():
   def __init__(self,name,second_name,f_name,age,Gradguation_document,Birth_place,current_address,document_percentage,chance,faculty,nationality):
        self.name=name
        self.second_name=second_name
        self.f_name=f_name
        self.age=age
        self.Gradguation_document=Gradguation_document
        self.Birth_place=Birth_place
        self.current_address=current_address
        self.faculty=faculty
        self.document_percetage=document_percentage
        self.chance=chance
        self.nationality=nationality
    
   def show_attend(self):
       

        if(self.Gradguation_document=='yes' and self.document_percetage>75 and self.chance<=3 and self.nationality=="Afghan" ):
            print(f"Welcome You cant attend in university and the faculity of :{self.faculty} ")
class pees():
    def __init__(self,pee):
        self.pee=pee
    
    def show_pee(self):
        if(self.pee==3500):
            print("You are pay one month pees:%d"%self.pee)
        elif(self.pee==7000):
            print("You are pay two Months pees:%d"%self.pee)
        elif(self.pee==10500):
            print("You are pay three Months pees:%d"%self.pee)
        elif(self.pee==14000):
            print("You are pay four Months pees:%d"%self.pee)
        elif(self.pee==17500):
            print("You are pay five Months pees:%d"%self.pee)
        elif(self.pee==21000):
            print("You are pay sex Months pees:%d"%self.pee)
        else:
            print("innvilide pees:")

class class_name_and_attendence_of_subjec():
    def __init__(self,class_name,programing,computer,islamic,math,pysic,tajwed,english,history):
        self.class_name=class_name
        self.programing=programing
        self.computer=computer
        self.islamic=islamic
        self.math=math
        self.pysic=pysic
        self.tajwed=tajwed
        self.english=english
        self.history=history
    def show_attendenc(self):
       # if(self.class_name=="M01" and self.programing>=75 and self.computer>=75 and self.islamic>=75 and self.math>=75 and self.pysic>=75 and self.tajwed>=75 and self.english>=75 and self.history>=75):
        #    print("You are can attend and examination ")
        #else:
         #   print("Your can,t attend in examinatin Because Your attendence is Not enough ")
        if(self.class_name=='M01'or self.class_name=='m4'or self.class_name=='m03'):
           print("You class is :%s"%self.class_name)
        elif(self.programing<75):
           print("YOu are mkhrom in  programing subjec:%d"%self.programing)
        elif(self.computer<75):
           print("You are makhrom in computer subject:%d"%self.computer)
        elif(self.islamic<75):
           print("You are makhrom in islamic subject:%d"%self.islamic)
        elif(self.english<75):
           print("You are makhrom in english subjec:%d"%self.english)
        elif(self.math<75):
           print("You are makhrom in math subject:%d"%self.math)
        elif(self.pysic<75):
           print("You are makhrom in pysic subject :%d"%self.pysic)
        elif(self.tajwed<75):
           print("You are makhrom in tajwade subject :%d"%self.tajwed)
        elif(self.history<75):
           print("You are makhrom in history subject :%d"%self.history)
        
class examination():
    Total_marks1=0
    percentage1=0
    Total_marks=0
    percentage=0
    programing1=0
    computer1=0
    math1=0
    islamic1=0
    pysic1=0
    tajwade1=0
    history1=0
    english1=0

    def midd_turm(self):
        
        self.programing1=int(input("Enter programing Marks:"))
        self.computer1=int(input("Enter the computer Marks:"))
        self.math1=int(input("Enter the math Marks:"))
        self.islamic1=int(input("Enter islamic Marks:"))
        self.pysic1=int(input("Enter the pysic Marks:"))
        self.tajwade1=int(input("Enter the tajwade Marks:"))
        self.history1=int(input("Enter the history Marks:"))
        self.english1=int(input("Enter the englisth Marks:"))
        if(self.programing1>20 or self.computer1>20 or self.english1>20 or self.history1>20 or self.islamic1>20 or self.math1>20 or self.pysic1>20 or self.tajwade1>20):
            print("Your marks out of Range [20]")
        else:
         self.Total_marks1+=self.programing1+self.computer1+self.math1+self.islamic1+self.pysic1+self.tajwade1+self.history1+self.english1
         self.percentage1=self.Total_marks1/8
         print("percentage:%d"%self.percentage1)
        
    
    def final_examination(self):
        self.programing=int(input("Enter programing Marks:"))
        self.computer=int(input("Enter the computer Marks:"))
        self.math=int(input("Enter the math Marks:"))
        self.islamic=int(input("Enter islamic Marks:"))
        self.pysic=int(input("Enter the pysic Marks:"))
        self.tajwade=int(input("Enter the tajwade Marks:"))
        self.history=int(input("Enter the history Marks:"))
        self.english=int(input("Enter the englisth Marks:"))
        self.Total_marks+=self.programing+self.computer+self.math+self.islamic+self.pysic+self.tajwade+self.history+self.english
        if(self.programing>80 or self.computer>80 or self.english>80 or self.history>80 or self.islamic>80 or self.math>80 or self.pysic>80 or self.tajwade>80):
         print("Your marks out of Range [80]")
        else:
         
          self.Total_marks+=self.Total_marks1
          self.percentage=self.Total_marks/8
          print("percentage:%d"%self.percentage)
          print("Your Total marks:%d"%self.Total_marks)

          if(self.programing<55):
            self.programing1+=self.programing
            
            print("Your fail in programing subject:%d"%self.programing1)
          elif(self.computer<55):
             self.computer1+=self.computer
             print("YOur fail in computer subjec:%d"%self.computer1)
          elif(self.islamic<55):
            self.islamic1+=self.islamic
            print("Your fail in islamic subjec :%d"%self.islamic1)
          elif(self.math<55):
              self.math1+=self.math
              print("Your fail in math subjec:%d"%self.math1)
          elif(self.pysic<55):
            self.pysic1+self.pysic
            print("Your fail in pysic subject :%d"%self.pysic1)
          elif(self.tajwade<55):
            self.tajwade1+self.tajwade
            print("Your fail in tajwade subjec:%d"%self.tajwade1)
          elif(self.history<55):
             self.history1+=self.history
             print("Your fail in history subjec:%d"%self.history1)
          elif(self.english<55):
            self.english1+=self.english
            print("Your fail in english subject :%d"%self.english1)



#obj2=examination()
#obj2.midd_turm()
#obj2.final_examination()




while 1:
   print("Welcome TO AFghan university")
   print("-----------------------------\n")
   print("1.For cankor exam Regestration")
   print("2.For admission")
   print("3.For attendence")
   print("4.For midd and finial exams")
   select=int(input("Select the option:"))
   print("--------------------------------")

   if(select==1):
      obj=Attend_in_university(name=input("Enter name:"),second_name=input("Enter the second name:"),f_name=input("Enter the fathe name:"),age=input("Enter the age:"),Gradguation_document=input("Enter gradguation document:"),Birth_place=input("Enter birth place:"),current_address=input("Enter current placce:"),document_percentage=int(input("Enter the percentage:")),chance=int(input("Enter chance:")),faculty=input("Enter the faculty :"),nationality=input("Ente the nationality:"))
      obj.show_attend()
   elif(select==2):
      obj=pees(pee=int(input("Enter pees:")))
      obj.show_pee()
   elif(select==3):
      object1=class_name_and_attendence_of_subjec(class_name=input("Enter the class name:"),programing=int(input("Enter the programing subect attendence percentage:")),computer=int(input("Enter the computer subect attendence percentage:")),islamic=int(input("Enter the istamic subect attendence percentage:")),math=int(input("Enter the math subect attendence percentage:")),pysic=int(input("Enter the pysic subect attendence percentage:")),tajwed=int(input("Enter the tajwed subect attendence percentage:")),english=int(input("Enter the English subect attendence percentage:")),history=int(input("Enter the history subect attendence percentage:")))
      object1.show_attendenc()
   elif(select==4):
      print("1.For midd term exam and 2.For final exam")
      select1=int(input("first of all You shold Give midd term then final Or your choice:"))
      
      obj2=examination()
      if(select1==1):
         obj2.midd_turm()
      elif(select1==2):
        obj2.final_examination()
      else:
         print("invilide select")
   else:
      print("invilide select")
      
         