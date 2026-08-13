# Parking project in python for improvement of function for beginner 

balance=0
total=0
total_vechical=0
total_car=0
total_bus=0
total_taxy=0
total_cycle=0
total_motarcycle=0
acount=0

def total(balance):
    balance


def total_cars(acount,total_vechical,total_car,total_bus,total_taxy,total_cycle,total_motarcycle):
   return acount,total_car,total_vechical,total_bus,total_taxy,total_cycle,total_motarcycle



def vechical(balance):
    balance
def  car(balance):
    balance
def  bus(balance):
    balance
def  taxy(balance):
    balance
def motarcycle(balance):
    balance
def cycle(balance):
    balance


while True:
    print("                                          WELCOME TO PARKING APPLICATION")
    print("------------------------------------------------------------------------------------------------------------")
    print("                                                HERE IS THE MENU ")
    print("                                                For total amount  prass:1   ")
    print("                                                For  vechile prass:2  ")
    print("                                                For car prass:3   ")
    print("                                                For taxy prass:4")
    print("                                                For motor cycle prass:5" )
    print("                                                For  cycle prass:6    ")
    print("                                                For total cars prass:7   ")
    num=int(input("                                                Selec the car:"))
    
    
    
    if (num==2):
      vechical(balance)
      num2=int(input("                                     For parking vechile (100):"))
      if(num2<100):
        print("                                          Your amount is not Enough:",num2)
      else:
        balance=balance+num2
        print(                                            "Your parking vechile By =",num2)
        total_vechical+=1
        print(" total vechical in the parking :%d"%total_vechical)
        acount+=1
        
    elif(num==3):
      car(balance)
      num2=int (input("                                            For parking car(50):"))
      if(num2<50):
          print("                                        Your amount is not Enought:",num2)
      else:
          balance+=num2
          print("                                           Your parking car By:",num2)
          total_car+=1
          print("total car in the parking :%d"%total_car)
          acount+=1
    elif(num==4):
      taxy(balance)
      num2=int(input("                                        For taxy parking (60):"))
      if(num2<60):
          print("                                             Your amount is not Enought:",num2)
      else:
          balance+=num2  
          print("                                            Your parking taxy by:",num2) 
          total_taxy+=1
          print("total taxy in the parking :%d"%total_taxy)
          acount+=1
    elif(num==5):
      motarcycle(balance)
      num2=int(input("                                     For motarcycle parking(20):"))
      if(num2<20):
          print("                                         Your amount is not Enough:",num2)
      else:
          balance+=num2
          print("                                        Your parking motarcycle By:",num2)
          total_motarcycle+=1
          print("total motarcycle in the parking :%d"%total_motarcycle)
          acount+=1
    elif(num==6):
      cycle(balance) 
      num2=int(input("                                     FOr cycle parking (10):"))
      if(num2<10):
          print("                                        Your amount is  not Enough")
      else:
          balance+=num2
          print("                                         Your parking cycle By:",num2)
          total_cycle+=1
          print("total cycle in the parking:%d"%total_cycle)
          acount+=1
    elif(num==1):
       total(balance)
       print("Your total parking :",balance)
    
    elif(num==7):
       total_cars(acount,total_vechical,total_taxy,total_cycle,total_bus,total_motarcycle,total_car)
       print("Your total cars in the parking :",acount)
       print("\nTotal vechical:",total_vechical,'\nTotal Taxy:',total_taxy,'\nTotal cycle:',total_cycle,'\nTotal bus:',total_bus,'\nTotal motarcyle:',total_motarcycle,"\nTotal car:",total_car)

     
     
     
     
     
     
     
     
      
            
          


        

    
    
   