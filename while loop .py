'''
playername='parveez'
counter=3
while True:
    userinput=input("enter the player:")
    if userinput=='parveez':
        print("you found the player he is ", playername)
        break
    else:
        counter=counter-1
        if counter>0:
            print("try again %c counter left",counter)
        else:
            print("the game over!!!!")
            print("you could,t find")
            break
'''
'''
n=7
i=1

while i<=10:
    print(f"{n}* {i}={n*i}")
    i+=1



n=10
i=1

while i<=10:
    print(f"{i}x{n}={i*n}")
    i=i+1


n=2
i=1

while i<=10:
    print(f"{i}x{n}={i*n}")
    i=i+1


n=3
p=1

while p<=10:
    print(f"{p}x{n}={p*n}")
    p=p+1


n=4
c=1

while c<=10:
    print(f"{c}x{n}={c*n}")
    c=c+1


n=6
q=1

while q<=10:
    print(f"{q}x{n}={q*n}")
    q=q+1


word='program'
count=0
i=0

while i<len(word):
    count+=1
    i+=1
    print("word",count)


n=0

while n<=10:
    print(n)
    n=n+1


row=5

i=1

while i<5:
    print("*"*i)
    i=i+1


def name_list():
    return["name:"]
def name_list1():
    return["parveez"]
def name_list2():
    return["afghan"]



sequence=name_list()+name_list1()+name_list2()

print(sequence)

for x in sequence:
    print(x)



def word_one():
    return "parveez"
def word_two():
    return "afghan"
def word_three():
    return "king"

sentence=f"{word_one()}{word_two()}{word_three()}"
print(sentence)

def word_one():
    return "parveez"
def word_two():
    return "afghan"
def word_three():
    return "king"
sentence=word_one()+word_two()+word_three()
print(sentence)

def part_one():
    return "python"
def part_two():
    return "is"
def part_three():
    return "fun!"

sequence=part_one() + part_two() + part_three()

print(sequence)






def addtion(a,b,c,d):
    return a+b+c+d

result=addtion(10,10,10,10)

print(result)



def multiflication(a,b,c,d):
    return a*b*c*d

result=multiflication(10,2,5,5)
print(result)


def substraction(a,b,c,d):
    return a-b-c-d

result=substraction(100,50,30,10)

print(result)


def division(a,b,c):
    return a/b/c
result=division(1000,10,2)

print(result)


n=0 

while n<=100:
    print("i love you my country",n)
    n=n+1

'''



for x in range(1,100):
    if(x==50):
        print(x)
        break