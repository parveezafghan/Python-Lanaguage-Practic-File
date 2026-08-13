'''
n=0
while n<10:
    print("welcome to paython series",n)
    n=n+2
    '''
'''
n=1
while n<=20:
    print("welcome to python",n)
    n=n+2
    if n>15:
        break
else:
    print("loop is ended")
'''
'''
playername="parveez"
while True:
    userInput=input("guess player name:")
    if userInput==playername:
        print("your found the player %s"%playername)
        break
    else:
        print("it is wronge enter ")
'''
'''
playername="parveez"
counter=3
while True:
    userinput=input("guess player name")
    if userinput==playername:
        print("coungratulation")
        print("you found the player he is , %s"%playername)
        break
    else:
        counter=counter-1
        if counter>0:

         print("it is wronge try again . you have only %d"%counter,"left")
        else:
           print("game is over")
           print(" you coudn't find")
           '''
'''
for x in range(10):
    if x==5:
        continue
    print(x)
else:
    print("loop is ended")
print("this is the rest of frogram".upper())
'''

# binary number system
# base 2 is the collection of 0,1
'''
n=0b101010
print(n)
'''
'''
#octal number system
# base 8 and it contain 0 to 7 values
b=0o324234
print(b)
'''
'''
#Decemal number system
#base 10 and it contain 0 to 9 values
g=23
print(g)
'''
'''
#hexadecimal number system
#base 16 and it contain 0 to 10+A to F values
s=0x3232
print(s)
'''
'''
def method ():
    print("hi this is method ")
    x=40
    y=50
    zz=(x+y)
    print(zz)

def method(id,name,salary):
    print("your id",id)
    print("your name",name)
    print("your salary",salary)


def mehtod4 (name,id=10,salary=666):
    print("your name;",name)
    print("your id:",id)
    print("your salary",salary)




mehtod4("parveez")
'''




