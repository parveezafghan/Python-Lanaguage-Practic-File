
'''
# normall or requird approch
def method (id,name):
    print("hi this is method")
    print("your id:",id)
    print("your name:",name)
# default approch
def method1 (id=10,name="parveez afghan"):
    print("hi this is method2")
    print("your id:",id)
    print("your name:",name)
# mix up approch example 
def method3(id,name="parveez afghan",):
    print("hi this is method3")
    print('your id:',id)
    print("your name:",name)
  # mix up approch example
def method4(id,name="parveez afghan",salary=500):
    print("hi this is mehtod4")
    print("your id :",id)
    print("your name :",name) 
    print("your salary:",salary)
# key word approch
def method5 (id,name,salary):
    print("your id:",id)
    print("your name:",name)
    print("your salary:",salary)
#method5(id=50,name="parveez afghan",salary=6000)
# variavle argoment approch
def method6(*var):
    print("hi this is method6")
    for y in var:
        print("value=",y)
    else:
        print("loop is ended")
#method6(23,45,65,76,)


def method7(name='parveez',*var):
    print('hi this is method7:')
    print('your name:',name)
    for x in var:
        print("value of x:",x)
    else:
        print("------------")


def method8(name,*var):
    print("method8")
    print("your name:",name)
    for y in var:
      print("value y:",y)
    else:
        print("loop is ended")
def method9(*var,name):
    print("method9")
    print("your name",name)
    for x in var:
        print("value:",x)
    else:
        print("loop is ended")



def method8(name,*var):
    print("this is method8")
    print("your name:",name)
    for x in var:
        print("value",x)

    else:
        print("loop is ended")


def method8(*var,name,salary,project):
    print("your name ",name)
    print("your salary",salary)
    print("your project",project)
    for y in var:
        print('value ',y)
    else:
        print("loop is ended")
    method8(10,398,38,name="parveez",salary=5888,project="database") 
# funtion return


# value hold by print in function
def method():
    return 100
def method1():
    return 200
#fist way
print(method())
print(method1())
# seceond way
y=method()
print(y)

x=method1()
print(x)

# argoment passing 


def add(x,y):
    return x+y
print(add(100,400))

def mul(x,y):
    return x*y
print(mul(10,50))

def division(x,y):
    return x/y
print(division(1000,2))

# in function returning we give two value which first return or second ignor 

def method():
    return 100
    return 'khan'
print(method())
def method1():
    return 100
    return 300
print(method1())

# if we hold a value in return and we don,t  value in return we will give None massege
def method():
    return 
y=method()
print(y) 

def method1():
    return 
x=method1()
print(x)
# the if statment to contorl the flow of multiple returning value



num=int(input("etner your number:"))
def comparison():
    if num>55:
        return "your success"
    else:
        return "your fail"
    


print(comparison())



def method56(x,y):
    if x>y:
        return "king"
    else:
        return "president"
    


print(method56(10,7))

'''







def 