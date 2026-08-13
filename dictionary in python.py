#Dictonar in python use to store data in the form of key and value.is also known items..\get() and keys[] are use to print key date from dictionary
#key must be unique and value can be duplicate/id memory addrees/is isnot coprison/== != data coprison/in not in for chicking data
#point to be noted 1.use to store value in the form of key & value pairs . 2 Dictionary mutable
#type()/we can print key and values/item use to print dictioary list then tuple/convert dictionar to list.tuple.set
#how to print date for dictionary/for loop.values.keys.items by two way/if we do add data to keys changable data is not allowed(list)
#dict()constrator of dictionary/zip as use joiner/if we have two list by zip we can join two list then convert to dictionary/
#unpicking a,d=dic(just key unpaking not value)/reassigning same to unpaking just elimint/we can add value by[2]=100/
#len for lenght/popitem()finl remove/pop(1)specific/clear/sorted.items.keys.value.None/invilide/valide/maximan/manimam
#join two dictonary by update or (**,**)/convert keys and value into list/copy./

'''
while True:
 fruit=input("Enter the name")
 fruit_price={"apple":5,"banana":10,"orange":15,'mango':30}



 def price(fruit):
  return fruit_price.get(fruit.lower(),"fruit price is not find")
 print(f"fruit price is {fruit}{price(fruit)}")

while True:


 user_input=input("Enter the name of studen:")
 employee={"parveez":["software engineer",'21 years old','study in software'],'amanullah':["medical doctor",'student in Nangrahar medical faculty ','19 years old','expert in Grammer'],'jamil':["parcmicitical doctor","student in rokhnan university",'19 years old'],'samullah':["studen in hada hight school ",'learing Enghlish',],'norullah':["student in  hada hight school ",'learning Enghlisth']}



 def finding(user_input):
    return employee.get(user_input.lower(),"studen is not find is sofware")




 print(f"your name is {user_input} {finding(user_input)}")
 '''

'''
while True:


 use_input=input("Enter the name of tools:")
 store={"laptap":10,'manator':20,'mouse':40,'keybord':100,'scaner':20,'motherbod':200}





 def count(store):
    return store.get(use_input.lower(),"is not find in stor")




 print(f"your tools{use_input} {count(store)}")


 

user_input=input("Enter the name of persion:")
phone_number_of_our_famile={"parveez":"0773417792",'jamil':"0771737485",'islam':'0778474270'}



def find():
    return phone_number_of_our_famile.get(user_input.lower(),'Number is not find')





print(f"your name {user_input}:and Number {find()}")
#print(user_input,find()) second way



while True:
 dictionar={"go":"move",
           "car":"vechile",
           "want":"desire",
           "fear":"threaten",
           }

 user_input=input("Enter word of find senonem:")


 def find():
    return dictionar.get(user_input)


 print(user_input,find())




dictionar={"king":["id=123",'salary=30000','age=21','expert in programing']}
user_input=(input("Enter the name of employee:"))


def find():
    return dictionar.get(user_input.lower(),"is not avalible")




print(f"your detials{user_input} {find()}")

'''



dicarionary={"parveez":["1.parveez"," 2.last name is Afghan"," 3.job software engineer"," 4.age 21 years old"],"amanullah":["1.amanullah"," 2.last name is :mobeen ","3.job doctor ","4. age 19 yeas old"],"jamil":["1.name :jamil ","2.last name is:khan","3.job doctor",'4.age 19 years old']}




def serching_information():
   serching=input("Enter the person name To find information:")

   if(serching in dicarionary):
      print(dicarionary.get(serching))
   else:
      print("include the corect information")


def show_person():
   print(dicarionary)




while(1):
   print("1.for find person information\n2.for show all person information")

   select=int(input("select the choice:"))

   if(select==1):
      serching_information()
   elif(select==2):
      show_person()
   else:
      print("invilide")