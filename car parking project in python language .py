total=0
amount_of_tax=0,amount_of_vechile=0,amount_of_motarcycle=0,amount_of_cycle=0
Total_cars=0,Total_taxy=0,Total_vechile_amount=0,Total_motarcycle_amount=0,Total_cycle_amount=0

class taxy:
    amount=0
    def __init__(self,taxy):
        self.taxy=taxy
    
    def tax(self):

        self.amount=self.taxy*50
        globals()['total']+=self.amount

        print("Your total parks cars :%d"%self.taxy,'and Your total taxy amount is :%d'%self.amount)

class vechile():
    amount1=0
    def __init__(self,vechile):

        self.vechile=vechile
    
    def vechile1(self):
        self.amount1=self.vechile*100
        globals()['total']+=self.amount1

        print("Your total vechile amount:%d"%self.amount1,"and Your total park cars:%d"%self.vechile)


class motarcycle():
    amount2=0
    def __init__(self,motarcycle):
        self.motarcyle=motarcycle
    
    def motarcycle1(self):
        self.amount2=self.motarcyle*20
        globals()['total']+=self.amount2
        print("your total parks cycle:%d"%self.motarcyle,'and Your total cycle amount is :%d'%self.amount2)

class cycle():
    amount3=0
    def __init__(self,cycle):
        self.cycle=cycle
    
    def cycle1(self):
        self.amount3=self.cycle*10
        globals()['total']+=self.amount3

        print("Your total parks cycle is :%d"%self.cycle,"and Your total cycle amount is :%d"%self.amount3)
class status():

    def show_status(self):
        print("Your total parking amount is :%d"%globals()['total'])
        

        

print("welcome to Afghan cars parking  ")
print("here is the manus")
print("1.for taxy  2. for vechle 3.motarcycle 4.for cycle .5 for status")
while 1:
    select=int(input("select the car to parks:"))

    if(select==1):
        object_of_taxy=taxy(taxy=int(input("Select the count of taxy:")))
        object_of_taxy.tax()
    elif(select==2):
        object_of_vechile=vechile(vechile=int(input("select the count of vechile:")))
        object_of_vechile.vechile1()
    elif(select==3):
        object_of_motarcycle=motarcycle(motarcycle=int(input("select the count of motarcycle:")))
        object_of_motarcycle.motarcycle1()
    elif(select==4):
        object_of_cycle=cycle(cycle=int(input("select the count of cycle:")))
        object_of_cycle.cycle1()
    elif(select==5):
        object_of_status=status()
        object_of_status.show_status()
    else:
        print("invildie number")