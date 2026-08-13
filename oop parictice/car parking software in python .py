Total_amount=0 

Total_cars=0
'''
Total_Raksha=0
Total_Raksh_amount=0
Total_Taxy=0
Total_Taxy_amount=0
Total_vechile=0
Total_vechile_amount=0
Total_motarcycle=0
Total_motarcycle_amount=0
Total_cycle=0
Total_cycle_amount=0
'''
class Raksh_park():
    Total_amount_of_Raksha=0
    Total_Raksha=0
    def __init__(self,Raksha_car):
        self.Raksha_car=Raksha_car
    

    def show_Raksha(self):
        self.Total_amount_of_Raksha=self.Raksha_car*50
        globals()["Total_amount"]+=self.Total_amount_of_Raksha
        self.Total_Raksha+=self.Raksha_car
        globals()["Total_cars"]+=self.Raksha_car

        print(f"Your Total Raksha:{self.Total_Raksha},Total Raksha amount:{self.Total_amount_of_Raksha}")
     

class Taxy_park (Raksh_park):
    Total_taxy=0
    Total_taxy_amount=0
    def __init__(self,Taxy_car):
        self.Taxy_car=Taxy_car
    
    def show_taxy(self):
        self.Total_taxy+=self.Total_taxy
        self.Total_taxy_amount=self.Taxy_car*30
        globals()["Total_amount"]+=self.Total_taxy_amount
        globals()["Total_cars"]+=self.Total_taxy
        print(f"Your Total Taxy is:{self.Taxy_car},Your Total Taxy amount is:{self.Total_taxy_amount}")

class vechile_park(Taxy_park):
    
    Total_amount_vechile=0
    Total_vechile=0
    def __init__(self,vechile_cars):
        self.vechile_cars=vechile_cars

    def show_vechile(self):

        self.Total_amount_vechile=self.vechile_cars*120
        self.Total_vechile+=self.vechile_cars
        globals()['Total_amount']+=self.Total_amount_vechile
        globals()["Total_cars"]+=self.vechile_cars

        print(f"Your Total vechile amount is :{self.Total_amount_vechile},and Your Total vechile is :{self.Total_vechile}")

class motarcycle_park(vechile_park):
    Total_amount_motarcycle=0
    Total_motarcycle=0
    def __init__(self,motarcycle_cars):
        self.motarcycle_cars=motarcycle_cars
   

    def show_motarcycle(self):
        self.Total_amount_motarcycle=self.motarcycle_cars*40
        self.Total_motarcycle+=self.motarcycle_cars
        globals()["Total_amount"]+=self.Total_amount_motarcycle
        globals()["Total_cars"]+=self.motarcycle_cars

        print(f"Your Total amount of motarcycle is :{self.Total_amount_motarcycle},and Your Total motarcycle is:{self.Total_motarcycle}")


class cycle_park(motarcycle_park):
    Total_amount_cycle=0
    Total_cycle=0
    def __init__(self,cycle_cars):
        self.cycle_cars=cycle_cars
    
    def show_cycle(self):
        self.Total_amount_cycle=self.cycle_cars*20
        self.Total_cycle+=self.cycle_cars
        globals()["Total_amount"]+=self.Total_amount_cycle
        globals()["Total_cars"]+=self.Total_cycle

        print(f"Your Total cycle amount is :{self.Total_amount_cycle},and Your Total cycle is :{self.Total_cycle}")
    

class status(cycle_park):
     
     
    
    def show_status_amount(self):
        print(f"Your Total amount of parking:{globals()["Total_amount"]}")
      #  print(f"Your Total park cars is :{globals()["Total_cars"]}")
        print(f"Your Total Raksha amount is :{super().Total_amount_of_Raksha}")
        print(f"Your total taxy amount of is:{super().Total_taxy_amount}")
        print(f"Your Total vechile amount is:{super().Total_amount_vechile}")
        print(f"Your Total motarcycle amount is:{super().Total_amount_motarcycle}")
        print(f"Your Total cycle amount is:{super().Total_amount_cycle}")
    def show_status_Total_cars(self):
        print(f"Your Total park cars is :{globals()['Total_cars']}")
        print(f"Your Total Raksha park Raksha is :{super().Total_Raksha}")
        print(f"Your Total park taxy is :{super().Total_taxy} ")
        print(f"Your Total park motarcycle is :{super().Total_motarcycle}")
        print(f"Your total park cycle is :{super().Total_cycle}")
        print(f"Your Total park vechile is:{super().Total_vechile}")


print("welecome to AFghan car parking software")
print("----------------------------------------------")
print("1.For cycle park \n 2.For taxy park \n 3.For vechile park\n 4.For motarcycle park\n 5.For Raksha park\n 6.For status")

while 1:
    select=int(input("Select the car To park:"))
    if(select==1):
        object=status(cycle_cars=int(input("Enter cycle coun of park:")))
        object.show_cycle()
    elif(select==2):
        object1=Taxy_park(Taxy_car=int(input("Enter the Taxy count To park:")))
        object1.show_taxy()
    elif(select==3):
        object2=vechile_park(vechile_cars=int(input("Enter the vechile count:")))
        object2.show_vechile()
    elif(select==4):
        object3=motarcycle_park(motarcycle_cars=int(input("Enter the count of motarcycle:")))
        object3.show_motarcycle()
    elif(select==5):
        object4=Raksh_park(Raksha_car=int(input("Enter the count of Raksha:")))
        object4.show_Raksha()
    elif(select==6):
        print("1.For Total cars amount\n 2.For Total cars")
        select1=int(input("Select the option:"))
        if(select1==1):
            object.show_status_amount()
        elif(select1==2):
            object.show_status_Total_cars()
        else:
            print("your option is invilide")
    else:
        print("invilide object your call")

