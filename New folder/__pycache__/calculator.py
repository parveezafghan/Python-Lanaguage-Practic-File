num1=int(input("enter you number:"))
num2=int(input("enter your number:"))
ope=(input("select operator [+,-,*,/,]"))

if(ope=='+'):
    result=num1+num2
    print("you total addition:",result)
elif(ope=='-'):
    result=num1-num2
    print("your total substration:",result)
elif(ope=='*'):
    result=num1*num2
    print("your total multiflication:",result)
elif(ope=='/'):
    result=num1/num2
    print("your total division:",result)
