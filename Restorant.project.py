

amount=0

def total(amount):
    amount
def sup(amount):
    amount
def salad(amount):
    amount
def chicken(amount):
    amount
def strick_Meat(amount):
    amount
def fish(amount):
    amount
def pizz(amount):
    amount
def kabaly_palu(amount):
    amount
while True:
     print("                          WELCOME TO AFGHAN RESTORANT")
     print("           -----------------------------------------------------------------")
  #   print("                                for chicking prass(1) ")
     print("                                Here is mainu")
     print("                                q for chick amount")
     print("                                sup:PRS=100  ")
     print("                                salad:PRS=50")
     print("                                chicken:PRS=250")
     print("                                strick meat:PRS=300")
     print("                                fish:PRS=150")
     print("                                 pizz:PRS=600")
     print("                                 kabaly palu:PRS=1200 ")
     print("            ---------------------------------------------------------------------                 ")
     selec=input("              # select the food:sup(s)salad(c)chicken(K)strick meat(r)fish(f)pizz(p)kabuly (k):")
     
     if(selec=="s"):
         sup(amount)
         num=int(input("                   Enter amount:")) 
         if(num<100):
             print(                  "you amount is not Enough =",num) 
         else:
             amount=num+amount
             print("                 you are buy one plate soup by=",num)
     elif(selec=='c'):
         salad(amount)
         num=int(input("                       Enter amont:"))
         if(num<50):
             print("                   your amont is not Enough =",num)
         else: 
             amount=num+amount
             print("                   your buy one plate salad by=",num)
     elif(selec=='K'):
         chicken(amount)
         num=int(input("                       Enter amount:"))
         if(num<250):
             print("                       your amount is not Enough =",num)
         else:
             amount=amount+num
             print(                       "your buy one chciken by=",num)
     elif(selec=='r'):
         strick_Meat(amount)
         num=int(input("                      Enter mount:"))
         if(num<300):
             print("                      your amount is not Enough=",num)
         else:
             amount=amount+num
             print("                         your buy strik meat by=",num)
     elif(selec=='f'):
         fish(amount)
         num=int(input("                       Enter amount"))
         if(num<150):
             print("                     your amount is not Enough=",num)
         else:
             amount=amount+num
             print("                      your buy fish by=",num)
     elif(selec=='p'):
         pizz(amount)
         num=int(input("                      Enter  amount"))
         if(num<600):
             print("                  your amount is not Enough=",num)
         else:
            amount=amount+num
            print("                   your buy one pizz by=",num)
     elif(selec=='k'):
         kabaly_palu(amount)
         num=int(input("                    Enter amount:"))
         if(num<1200):
             print("                 your amount is not Enough=",num)
         else:
             amount=amount+num
             print("              your buy one plate kabuly palu by=",num)

    
     elif(selec=='q'):
         total(amount)
         print("your total amount from selling Restorant=",amount)



