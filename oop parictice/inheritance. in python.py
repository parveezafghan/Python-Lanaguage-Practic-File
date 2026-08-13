'''
class squre():
    def __init__(self):
        self.num=int(input("Enter the number:"))

    def show(self):
        return self.num**2


obj=squre()
print("squre:",obj.show())
print('---------------------------------------------------')



class larget_number():
    def __init__(self):

        self.num=int(input("Enter the number:"))
        self.num1=int(input("Enter the second number:"))
    
    def show2(self):
        return max(self.num,self.num1)

obj=larget_number()
print(obj.show2())
print('-----------------------------------')



class min_number():
    def __init__(self):
        self.num=int(input("Enter the first numbe;"))
        self.num1=int(input("Enter the second number;"))
    def show4(self):
        return min(self.num,self.num1)




obj5=min_number()
print('minnam number:',obj5.show4())
'''


class chick_numbe():
    def __init__(self):
        self.num=int(input("Enter the number:"))
    

    def show5(self):
        return "even" if self.num%2==0 else "odd"


while True:
 obj5=chick_numbe()
 print(obj5.show5())