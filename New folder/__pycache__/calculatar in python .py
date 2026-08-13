#calculator 
add=0
sub=0
mul=0
div=0
rem=0
def addition(add):
     add

def substration(sub):
    sub

def multiflication(mul):
    mul

def division(div):
    div

def reminder(rem):
    rem

while True:
    print("                                                   CALULATOR")
    print("________________________________________________________________________________________________________")
    print("                                                selec the operation")
    print("                                                For addition prass 1:")
    print("                                                For substration pras 2:")
    print("                                                For multiflication prass 3:")
    print("                                                For division prass 4:")
    print("                                                For reminder prass 5:")
    print("__________________________________________________________________________________________________________")
    selec=int(input("                                                Selec the operation:"))
    if(selec==1):
        addition(add)
        num=int(input("Enter first number:"))
        
        num3=int(input("Enter second:"))
        add=num+num3
        print("you total adition:",add)
    elif(selec==2):
        substration(sub)
        num=int(input("Enter first number:"))
        
        num3=int(input("Enter second number:"))
        sub=num-num3
        print("Your total substration:",sub)
    elif(selec==3):
        multiflication(mul)
        num=int(input("Enter first number:"))
        num1=int(input("Enter second number:"))
        mul=num*num1
        print("Your total mul:",mul)
    elif(selec==4):
        division(div)
        num=int(input("Enter first number:"))
        num1=int(input("Enter second number:"))
        div=num/num1
        print("Your total division:",div)
    elif(selec==5):
        reminder(rem)
        num=int(input("Enter the first number:"))
        num1=int(input("Enter the second number:"))
        if(num%num1==0):
            print("the number is odd=",num)
        else:
            print("the number is even=",num)

