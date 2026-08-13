# while loop use to control flow of statement.which execute of code repetidly
# in three condition it can,t execute 1.execiption come to code/2.when come to break in our code/3 when vertual mechine shout down 
'''
import os
num=int(input("Enter the number:"))
num1=int(input("Enter the number:"))


while num<=num1:
    print("WELCOME TO AFGHNISTAN:%d"%num)
    num+=1
    if(num==20):
        os._exit(0) #vetual mechine shoul down

n=1
while n<=20:
    print(n)
    n+=2 
    if(n==10):
        break # break state not allow to print else statment
else:
    print("loop  is ended")




num=int(input("Enter the number:"))
num2=int(input("Enter the number:"))

while num<=num2:
    print(num/0)# exieption come to statement
    num+=1


while True:
 num=int(input("Enter the number:"))
 for x in range(1,10):
    print(f"{x}x{num}={x*num}")
'''
'''

playername='parveez'
attempt=3
while True:
    playername=input("Enter the name:")
    if(playername=="parveez"):
        print("congratulation")
        print("your find the player:")
        break
    else:
        attempt-=1
        

        print("Try again", attempt ,"left")
        if(attempt<=0):
         break
'''

'''

totol=0
num=0
totol1=0
totol2=0
while num<=10:

    print(num)
    num=num+1
    totol=totol+num
    if(num%2==0):
        totol1=totol1+num
    if(num%3==0):
        totol2=totol2+num
        
        

print("total ",totol)
print("even adition",totol1)
print("odd adition",totol2)
  '''
'''
attempt=3
while True:
    paswword=int(input("Enter the password:"))
    password=input("Enter the name password:")
    if(paswword==123 and password=="parveez"):
        print("welcome to system")
        break
    else:
        attempt=attempt-1
        print(f"your {attempt} left stay"y)
        if(attempt==0):
            print("close")
            break
     '''


'''

amount=10000
withraw=0


withraw=int(input("Enter the amount:"))

if(withraw>amount and withraw<1000):
    print("your can withrwa ")

else:
    print("you can")

    '''
'''
try1=3
while True:
    pass1=int(input("Enter your password:"))
    pass22=input("enter your second password:")
    if(pass1==123 and pass22=='parveez'):
        print("your can access to system")
        break
    else:
       try1-=1
       print("your attempt stay%d"%try1,"left")

       if(try1==0):
           print("finish procdure")
           break
   '''        







''''
print("parveez ",'king','mobeen','lala','jamil','amanullah',sep="              ")

'''

x=0b11010