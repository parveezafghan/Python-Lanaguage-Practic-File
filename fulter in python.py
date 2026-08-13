#the filter method filters the given sequence  with the help of a function that teats each element in the sequence
# to be true or not 
#
'''
list1=[1,2,3,4,5,6,7,8,9,10,12,13]


def fdv(x):
    if(x%3==0):
        return True
    else:
        return False
    



#odd=list(filter(fdv,list1))
#print(odd)
    
print(list(filter(fdv,list1)))



namelist=['parveez','king','mobeen','afghan']


print(list(filter(lambda x:x=="parveez",namelist)))
print(list(filter(lambda x:x=="king",namelist)))
print(list(filter(lambda x:x=="mobeen",namelist)))
print(list(filter(lambda x:x=='afghan',namelist)))

namelist=['parveez','king','mobeen','afghan']


def  name1(name):
    if(name=='parveez'):
        return True
    else:
        return False



print(list(filter(name1,namelist)))

vowel=["a","e","i",'o','u']

while True:
    user_input=input("Enter the word:")
    def test(ch):
        if(ch in vowel):
            return True
        else:
            return False

 

    list1=[]
    for x in user_input:
        list1.append(x)
    resul=(list(filter(test,list1)))


    if len(resul)==0:
        print("your word not have vowel letter",resul)
    
    else:
        print("your word contins",resul)



list1=["king",'mobeen','afghan']

while True:
    name=input("Enter the name:")
    print(list(filter(lambda x:x==name,list1)))



list1=[]
for x in range(1,100):

    list1.append(x)

    num=int(input("Enter the number:"))

    print(list(filter(lambda x:x==num,list1)))



while True:



 list1=[]
 for x in range(1,100):
    list1.append(x)


 user_input=int (input("Enter the number:"))



 print(list(filter(lambda x:x==user_input,list1)))
 '''


while True:
 x=input("Enter the name of check the Grade:")
 grade={"ahamad":"A Grade","king":"B Grade","mobeen":'C Grade','parveez':"A Grade"}


 def find(x):
  return grade.get(x,'not find grade')
 



 print(f"your Grade is {x} {find(x)}")
 