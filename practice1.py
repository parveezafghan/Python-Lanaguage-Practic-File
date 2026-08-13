'''
# first example 
fr=float(input("enter tempreture in (fr):"))
cent=5.0/9.0*(fr-32)
print("firenhit converto centigrade:",cent)



#second exmple
x=int(input("enter your number:"))
y=int(input("enter your number:"))
z=int(input("enter your number:"))


if(x>y):
    if(x>z):
        print('x is largest number',x)
else:
    if(y>x):
        if(y>z):
            print("y is largest number",y)
        else:
            if(z>x):
              if(z>y):
                print("z is the largest number:",z)      

       

# third example
num1=int(input("enter your number:"))
num2=int(input("enter your number:"))
num3=int(input("enter your number:"))
num4=int(input("enter your number:"))

if(num1>num2):
    if(num1>num3):
        if(num1>num4):
            print("num1 is greader:",num1)
else:
    if(num2>num1):
        if(num2>num3):
            if(num2>num4):
                print("num2 is greader:",num2)
    else:
         if(num3>num1):
            if(num3>num2):  
                if(num3>num4):
                    print("num3 is greader:",num3)
         else:
            if(num4>num1):
                if(num4>num2):
                    if(num4>num3):
                        print("num4 is greader:",num4)                                   
fr=float(input("enter tempreture in (fr):"))
cent=5.0/9.0*(fr-32)
print("firenhit converto centigrade:",cent)


#forth example
gen=(input("enter your gender"))
if gen=="m":
    print("your male")
elif gen=="f":
    print("your famle")

age=int(input("your age:"))
if age>20:
    print("your have allwo to Go")
elif age<20:
    print("your don,t have allow to Go")

pass1=(input("do your have passfort:"))
if(pass1=="yes"):
    print("your have allow to Go")
elif pass1=="no":
    print("your don;t have allow to Go")

id=(input("do your have id:"))
if(id=="yes"):
    print("your have allow to Go ")
elif id=="no":
    print("your don;t have allow to Go")

t=(input("do your have ticket:"))
if t=="yes":
    print("your have allow to Go ")
elif t=="no":
    print("your don't have allow to Go")

#sexth example
num=int(input("enter your number:"))
if(num>0):
    print("this is positive ")
if(num<0):
    print("this is negitive")
if (num%2==0):
    print("this is odd ")
    print("this is divisible on 2")
if(num%3==0):
    print("this is even number")
    print("this is divisible on 3")
if(num%7==0):
    print("this is divisilb on 7")
    '''
'''
opr=input("enter the operator:")
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))



if(opr=='+'):
    result=num1+num2
    print("adition of num1 and num2=",result)

elif(opr=='-'):
    result=num1-num2
    print("substration of num1 and num2=",result)

elif(opr=='*'):
    result=num1*num2
    print("multiflication of num1 and num2=",result)

elif(opr=='/'):
    result=num1/num2
    print("division of num1 and num2=",result)

    '''
'''
salary=int(input("enter the salary:"))
grade=int(input("enter the grade:"))

if(grade>15):
    bo=salary*50/100
    salary=salary+bo
    print("your bonus",bo)
    print("your total salary ",salary)


else:
    bo=salary*50/100
    salary=bo+salary
    print("your bonus:",bo)
    print("your total salary:",salary)
'''

sup=50
salad=20
chicken=100
amount=0

def total(amount):
    amount#=int(input("Ente the amount:"))
def sup(amount):
    amount

def salad(amount):
    amount

def chicken(amount):
    amount
while True:
    print("                                         Welcome to Afghan Restorant")
    print("                                 =================================================")
    print("                                                   Main manue    ")
    print("                                                    Sup:PRS=50")
    print("                                                    Salad:PRS=20 ")
    print("                                                    Chicken:PRS=100")
    print("                                  ===================================================")
    opr=input("                                Selec the (s for sup/ c for salad/ k for chicken,for total f):")
    if(opr=='s'):
        sup(amount)
        num=int(input("Enter amount:"))
        amount=amount+num
    elif(opr=='c'):
        salad(amount)
        num=int(input("Enter amount:"))
        amount=amount+num
    elif(opr=='k'):
        chicken(amount)
        num=int(input("Enter the amount:"))
        amount=amount+num
    

    elif(opr=='f'):
        total(amount)
        print("your total=",amount)













