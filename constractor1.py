#constractor use to writer the logic .it execute the when your make the object of class
# def __init__ (self):/it can directly calling
#if we want to change the class variable we use this trike.    self.name=name







'''
class mclass:
    name='king'
    def __init__(self,name):
        print("THIS is ",name)
        print("this is ",self.name)

        self.name=name           # it chagee king to prveez which accesable in the whole class




    



    def method(self):
        print("thi is method /",self.name)





obj=mclass('parveez')
obj.method()
                                            

    '''

name='parveez king'
class mclass():

    def method(self,id,address):
        self.id=id
        self.address=address
        print("my name is ",globals()["name"])
        print("MY id is ",self.id)
        print("My address is  ",self.address)


class mclass1(mclass):
    def method1(self):

        print("my name is ",globals()["name"])
        print("My id is ",super(),id)







obj=mclass1()
print(obj.method1())


