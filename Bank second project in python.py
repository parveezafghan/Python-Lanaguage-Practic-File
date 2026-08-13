
Total_amount=0
user_name=[]
user_password1=[]



def creat_account_in_BanK():
    user_name1=((input("Please Yuour full name::")))
    password=int(input("Please Your password:"))
    age=int(input("Please Your Age:"))
    id_card=input("Please Your nationalility:")
    if(id_card=="Afghan" or id_card=="AFGHAN" or id_card=="afghan"):
     print(f"Your Account name is:{user_name1}: Your Account password is:{password}: Your Age is:{age} And Your Nationalitiy is :{id_card}")
     user_name.append(user_name1)
     user_password1.append(password)
    else:
       print("please Your can,t creat account in Bank You must have nationality of Afghanistan Your Inter :%s"%id_card,"invilide nationility")


def Total_ammount_detial():
   print(f"Your Total amount in Account:{Total_amount}")


def widhraw_ammount_from_ammount():
   widhraw=int(input("Enter The amount You want To widhraw form Your Account"))
   if(widhraw>Total_amount):
      print("Your amount is out of Range Your Total Account amount is :(%d)"% Total_amount," And Your are Enter This Amount:(%d)"% widhraw)
   elif(widhraw<=Total_amount):
      tax=widhraw*10/100
     # widhraw-=tax
     # globals()['Total_amount']-=widhraw
      globals()['Total_amount']-=tax
      globals()['Total_amount']-=widhraw
      print('Your widraw Amount is :%d'%widhraw,"And Your widhraw tax is :%d"%tax,"And Your Total Amount of account is:%d"%globals()['Total_amount'])


def deposite_amount_To_account():
   deposit=int(input("Enter the amount is To add:"))
   if(deposit<0):
      print("You Amount is not Correct Your most Enter the positive:")
   elif(deposit>0):
      print("Your Enter Amount is:%d"%deposit)
      #Total_amount=Total_amount-deposit
      tax=deposit*10/100
      deposit-=tax
      globals()['Total_amount']=+deposit
      #globals()['Total_amount']=deposit
      print(f"Your deposite Amount is :{deposit} And Your Tax is:{tax} And Your Total Amount is:{globals()['Total_amount']}")



while 1:
   print("\t\t\tWelcome To centeral Bank")
   print("\t\t\t1.For Creation Account")
   print('\t\t\t2.For Total Amount')
   print("\t\t\t3.For widraw Amount")
   print("\t\t\t4.for deposite Amount")
   select=int(input("\tSelect the option:"))
   if(select==1):
      creat_account_in_BanK()
   elif(select==2):
      name=input("Enter Your account name:")
      if(name in user_name):
      
      
            Total_ammount_detial()
   
         
      else:
         print("Your account is not avalible in The Bank")
   elif(select==3):
      name=input("Enter the name of Account:")
      if(name in user_name):
         widhraw_ammount_from_ammount()
      else:
         print("Your Account is not avalible in The Bank")
   elif(select==4):
      name=input("Enter The name of Your Account:")
      if(name in user_name):
         deposite_amount_To_account()
      else:
         print("Your Account is not avalible in The Bank")
   else:
      print("Your select The Correct option")