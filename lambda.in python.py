#lambda is a small function.
# A lambda function is a samll anonyomous function alambda function can take and number f arguments,but can 
#only have one expression
'''


def mathod(x):
    print(x*2)



mathod(5)
print(mathod)



y=lambda n:n*2


print(y(2))


z=lambda y,x: x if x>y else y


print(z(10,20))



while True:


 n=int(input("Enter the number:"))

 even=lambda x: x%2==0

 print(even(n))



 if(even(n)):
    print("even number")
 else:
    print("ODD number")


    '''


while True:
 
 num=int(input("Enter the number:"))
 def function(x):
    return lambda  y:y*x


 double=function(2)
 thriple=function(3)
 fourthTime=function(4)


 print(double(num))
 print(thriple(num))
 print(fourthTime(num))