'''
rol=int(input("enter rolnumber:"))
name=input("enter you name:")
fname=input("enter you fname:")

it=int(input("it score:"))
pro=int(input("programing score:"))
eng=int(input("english score:"))
history=int(input("history score:"))
math=int(input("math score:"))
islamic=int(input("islamic score:"))

result=it+pro+eng+history+math+math+islamic
per=result/6

print("your percentage",per)


x=int(input("first number:"))
y=int(input("second number:"))


sum=x+y
print(sum)


sub=x-y
print(sub)

mul=x*y
print(mul)

div=x/y

print(div)



# dolar conversion to af,pk

s=int(input("amount of dolar:"))




a=s*75

f=s*250



print("1 dorlar become ",a)

print("1 dolar becom ",f)

'''
'''

def method():
    return "parveez"
def method1():
    return "king"
def method2():
    return "afghan"

sequence=method()+method1()+method2()

print(sequence)

'''

'''
tool=['computer','mouse','cabel','minetor','lodspeker']
#tool=int(input("select the tools:"))
while True:
    tool=(input("select the tools:"))
    if(tool==tool):
        
        if(tool=="lodspeker"):
            print("your stor completly finist")
            break

'''
player='parveez'
damage=3

while True:
    player=input("enter the player name:")
    if(player=="parveez"):
        print("welcome")
        print("congratulation")
        break
    else:
        damage=damage-1
        print("your damage %d ",damage,'left')
        if(damage==0):
            print("your damage")
            break




damage=10
counter=10
damage=int(input("enter your fire:"))
while True:
    if(damage==10):
        print("your are dead")
        break
    else:
        while True:
          counter=counter-1
          print("your blood is %d",counter,'left')
          if(counter==0):
           break
          


    break
        




name=['computer','computer','tool','memory']

name=input("enter the toolsnmae:")
while True:
   print("yout finid ",name,"left")
   if(name=="memory"):
      
    print("finish")
   break
   

   