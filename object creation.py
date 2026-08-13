# in the python we can use two ways of makeing objcet of class 
# named object /obj=mclass/ obj.method()
# nameless object/ mclass().method()
# in the calling time we can change the value of objec/ entity the value of class is change just change the object values


'''
class mclass:
    name='parveez '
    second_name='afghan'
    def method(self):
        print("My name is ",self.name,"and My second name is ",self.second_name)

    

    def method1(self):
        id=100
        salary=1000
        print("My id is :",id,"and My salary is:",salary)
    
class mmclass:
    Grade="A"
    position=1
    def mehtod(self):
        print("My Grade is ",self.Grade,"and My position is ",self.position)
    


class place:
    current_addres="Nangrahar"
    previous_addres='pakty'

    def method(self):
        print('My curren addres:',self.current_addres,"and my prevous addres is ",self.previous_addres)



'''
''''
obj=mclass()
obj.method()
obj.method1()

obj2=mmclass()
obj2.mehtod()


obj3=place()
obj3.method()
'''

'''
mclass().method() 
mclass().method1()

mmclass().mehtod()

place().method()

'''


n=100

print(bin(n))