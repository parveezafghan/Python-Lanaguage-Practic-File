'''
attempt=3
while True:
 password_number=int(input("Enter the number pssword:"))
 password_al=input("Enter the strange password:")
 if(password_number==123 and password_al=='parveez'):
  print("Welcome to system")
  break
 else:
  attempt-=1
  print("your attempt %d"% attempt,"left")
  if(attempt==0):
   print("the system is off")
   break
  '''
'''
while True:
 id_card=(input("show the id card(Yes or no):"))
 pssport=input("show the passport(Yes or no)")
 age=int(input("Enter your age:"))
 Gender=input("Enter your Gender(male or famel)")
 ticket=input("show the ticket(Yes or no):")
 if(id_card=='yes' and pssport=='yes' and age>=18 and Gender=='male' and ticket=='yes'):
  print("your can Go")
 else:
  print('You can,t GO')
'''
'''

while True:
 camer_pasword=int(input("Enter the General password:"))
 use_password=input("Enter the strange password for user :")
 chack_camera=int(input("Enter the camera number:"))

 if(camer_pasword==122 and use_password=='parveez' and chack_camera <=5 ):
    print("system is normall you can user system")

 else:
    print("chek the system ")


    '''
''''
while True:
    shop_size=(input("Enter the size of shop:"))
    location_shop=input("Enter the location of shop:")
    monthly_sells=int(input("Enter the monthly sells:"))
    if(shop_size=="Big" and location_shop=='city' or (monthly_sells==100000)):
        print("your are eligible of pay tax")
        
    else:
        print("your not eligible to pay tax")

'''
        

id=int(input("Enter id"))
name=input("Enter name:")
last_name=input("Enter last name:")
nationality=input("Enter nationality :")
id_card=input("enter id card:")
Gender=input("Enter Gender:")
pass1=input("Enter passport")
if(id==123):
    if(name=="parveez"):
        if(last_name=="AFghan"):
            if(nationality=="AFghan"):
                if(id_card=="T"):
                    if(Gender=='famale' or Gender=='male'):
                        if(pass1=="yes"):
                            print("You are can go")
                        else:
                            print("invilide passport")
                    else:
                        print("invilide Gendr")        
                else:
                    print("invildi di card")            
            else:
                print("invilde natonality")                
        else:
            print("invilid last name")                    
    else:
        print("invilid name")                        
else:
    print("invilid id")                            