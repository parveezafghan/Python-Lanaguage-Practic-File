
def add(a,b):
    return a+b

def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

while True:
    print("                                            CALCULATOR")
    print("                                      selec the operation:")
    print("                                           1.add") 
    print("                                           2.substration")
    print("                                           3.multiflication")
    print("                                           4.division")
    print("==================================================================================================")
    selec=int(input("                                        Selec the operation:"))
    num1=float(input("Enter firs number:"))
    num2=float(input("Enter second number:"))
    if(selec==1):
      print(f"{num1}+{num2}={add(num1,num2)}")

    elif(selec==2):
        print(f'{num1}-{num2}={sub(num1,num2)}')
    elif(selec==3):
        print(f'{num1}*{num2}={mul(num1,num2)}')
    elif(selec==4):
        print(f"{num1}/{num2}={div(num1,num2)}")


