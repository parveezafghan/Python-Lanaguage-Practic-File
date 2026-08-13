class add_numbe():

    def __init__(self):
        self.num1=int(input("Enter the first number;"))
        self.num2=int(input("Enter the secon number:"))

    def show(self):
        return self.num1+self.num2


class mul():
    def __init__(self):
        self.num1=int(input("Enter the firs number:"))
        self.num2=int(input("Enter the second number:"))

    def show1(self):
        return self.num1*self.num2

class division():

    def __init__(self):
        self.num1=int(input("Enter the number1:"))
        self.num2=int(input("Enter the seocn number:"))

    def show3(self):
        return self.num1/self.num2

class sub():
    def __init__(self):
      self.num1=int(input("Enter the first number:"))
      self.num2=int(input("Enter the secon number;"))

    def show4(self):
        return self.num1-self.num2

obj=add_numbe()
print("adition of two number:",obj.show())
print("---------------------------------")
obj1=mul()
print("this is the mul two number:",obj1.show1())
print("---------------------------------------------")
obj3=sub()
print("this is the sub:",obj3.show4())
print('-------------------------------------------')
obj2=division()
print("this is division:",obj2.show3())