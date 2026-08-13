class Box:

    withd,heith=0,0


class TDBox(Box):
    color="Green"
    def __init__(self,withd,heith):
        self.withd=withd
        self.heith=heith
        self.color

    
    def diplay(self):

        print(f"Box withd{self.withd},Box heith{self.heith},Box color{self.color}")

        print("BOx area:",self.withd*self.heith)

class ThreeBox(TDBox):
    axix=0

    def __init__(self,w,h,z):

        self.withd=w
        self.heith=h
        self.axix=z
    
    def diplay3(self):
        print("zaixix:",self.withd*self.heith*self.axix)
        print(f"with{self.withd},heith{self.heith},color{self.color}  self zxix{self.axix}")
    def change_coloer(self,color):
        self.color=color
obj=TDBox(7,9)
obj.diplay()
print("_____________________")

obj1=ThreeBox(5,3,2)
obj1.change_coloer("Red")
obj1.diplay3()