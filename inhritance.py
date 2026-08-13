class A:

    def display(self):
        print("from A class ")

class B(A):

    def display1(self):
        print(" for B class")


class C:

    def display2(self):
        print("for C class")


class D(B,C):
    def display3(self):
        print(" for D class")



obj=D()

obj.display()
obj.display1()
obj.display2()
obj.display3()