'''
salary=int(input("enter the salary:"))
age=int(input("enter the  age:"))

if(salary>10000):
    if(age>25):
        print("you should pay income  tax")
    else:
        print("you don,t have tax")

else:
    print("you don,t have tax")


gender=input("your gender male or famle:")
pass1=(input("are your have passport yes or no:"))
ticket=input("are you have ticket yes or no:")
id=input("are you have id  card yes or no:")

if(gender=='male'):
    print("you are male")
if(gender=='famle'):
    print("you are famle")
if(pass1=='yes'):
    print("you can go")
if(pass1=='no'):
    print("you con,t go")
if(ticket=='yes'):
    print("you can go")
if(ticket=='no'):
    print("you can,t go")
if(id=='yes'):
    print("you can go")
if(id=='no'):
    print("your can,t go")


opr=input("enter the opr")
num1=float(input("enter number1:"))
num2=float(input("enter number2:"))


if(opr=='+'):
    result=num1+num2
    print("you total adition",result)
elif(opr=='-'):
    result=num1-num2
    print("your total substraction:",result)
elif(opr=='*'):
    result=num1*num2
    print("your total multiflication:",result)
elif(opr=='/'):
    result=num1/num2
    print("your total division:",result)

#convert selisus to pernhit
tem=int(input("enter the tempreturn in selisus:"))

def selisus(se):
    return se*9/5+32

print(selisus(tem))


# conver pernhit to selisus

per=int(input("enter the pernhit:"))
def pernhit_to_selisus(per):
    return per*5/9+32


print(pernhit_to_selisus(per))


num=int(input("enter the number:"))
def multiflication(num):
    return num* 10

print(multiflication(num))


tem=int(input("enter the tempreture in selisus:"))

selisus=tem*9/5+32
print("tempreturn in prenhit:",tem)


age=int(input("enter the age:"))

if(age>1 and age<=14):
    print("you are adult:",age)
elif(age>14 and age<=40):
    print("you are younge:",age)
elif(age>40 and age<=60):
    print("you are near to oldist life:",age)

elif(age>60 ):
    print("you are in old life")



                                                   
print(".1.adition:")
print(".2.substriction:")
print(".3. multiflication:")
print('.4. division:')
num=int(input("select the option"))


if(num==1):
    num1=int(input("enter the number:"))
    opr=input("select the operator:")
    num2=int(input("enter the number:"))
    adition=f'{num1}+{num2}={num1+num2}'
    print("adition+",adition)

elif(num==2):
    num1=int(input("enter the number:"))
    opr=input("enter the operator:")
    num2=int(input("enter the number:"))

    sub=f'{num1}-{num2}={num1-num2}'
    print('substriction:',sub)

elif(num==3):
    num1=int(input("enter the number:"))
    opr=int(input("enter the operatior:"))
    num2=int(input("enter the number:"))
    mul=f'{num1}*{num2}={num1*num2}'
    print("multiflication:",mul)

elif(num==4):
    num1=int(input("enter the number:"))
    opr=(input("enter the operator:"))
    num2=int(input("enter the number:"))
    div=f'{num1}/{num2}={num1/num2}'

    print("division:",div)



print(".+.adition:")
print(".-.substriction:")
print(".*. multiflication:")
print('./. division:')

opr=input("enter the operator:")
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))

if(opr=='+'):
    result=num1+num2
    print("total adition:",result)
elif(opr=='-'):
    result=num1-num2
    print('substricton:',result)
elif(opr=='*'):
    result=num1*num2
    print("total multiflication:")
elif(opr=='/'):
    result=num1/num2
    print("division:",result)

 
import time

while True:
    def red():
        time.sleep(3)
        print("STOP")
    def yellow():
        time.sleep(3)
        print("READY FOR MOVING ")
    def green():
        time.sleep(3)
        print("GO")

        



    

    red()
    yellow()
    green()

'''

while True:
    
 num=int(input("Enter the number:"))

 for x in range(1,11):
        print(x,"x",num,"=",x*num)
    