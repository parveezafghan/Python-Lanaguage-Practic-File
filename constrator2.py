


while True:
 class op:
    value1=int(input("Enter the number:"))
    value2=int(input("Enter the number:"))

    def __init__(self,value1,value2):
      print("WELCOME TO OPEATION CLASS")
      self.value1=value1
      self.value2=value2



    
    def add(self):
      print("Total adition:",self.value1+self.value2)

    
    def sub(self):
      print("TOtal substration :",self.value1-self.value2)


    def mul(self):
      print("Total multiflication:",self.value1*self.value2)


    def div(self):
      print("Total division:",self.value1/self.value2) 






    obj=op(value1,value2)
    obj.add()
    obj.sub()
    obj.mul()
    obj.div ()
