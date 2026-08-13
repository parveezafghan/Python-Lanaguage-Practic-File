

'''
num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
num3=int(input("Enter the number3:"))
num4=int(input("Enter the number4:"))


math=lambda num1,num2,num3,num4:num1*num2*num3*num4

print(math(num1,num2,num3,num4))


x=int(input("Enter the Number:"))


math=lambda x:x%2==0


print(math(x))
'''

'''
number=int(input("Enter the number:"))


math=lambda number:number**2


print(math(number))
'''
'''
y=int(input("Enter the number:"))
x=int(input("Enter the number:"))

math=lambda y,x:y if y>x else x

print(math(y,x))
'''
'''

list1=[1,2,3,4,5,6,7,8,9,10]




print(list(filter(lambda x:x%2==0,list1)))

print(list(filter(lambda x:x%3==0 ,list1)))

print(list(filter(lambda x:x%4==0,list1)))

'''


km=int(input("Enter the km:"))



m=1000*km
cm=100000*km
mm=1000000*km

print("km convert to m:%d "%m)
print("km convert to cm %d"%cm)
print("km convert to mm:%d"%mm)




