
#            not complet project 



while True: 
 Total_vechile=0
 Total_taxy=0
 Total_motarcycle=0
 Total_cycle=0
 def Total_cars(Total_vechile,Total_taxy,Total_cycle,Total_motarcycle):
   return Total_cycle,Total_taxy,Total_vechile,Total_motarcycle
 
 def shop(tax,vechile,motarcycle,cycle):
    return tax,vechile,motarcycle,cycle
 
 print("                                    WELCOME TO BARGINE SHOP")
 print("___________________________________________________________________________________")
 print("                                        Here is the menue   ")
 print("                                        Taxy price 1000&       ")
 print("                                        Vechile price 4000&  ")
 print("                                         Motarcycle price 200&          ")
 print("                                         cycle price   100&            ")
 print("                                           For Total cars 6")
 print("______________________________________________________________________________________     ")
 print("                                             for tax 1 for vechile 2 for motarcycle 3 cycle 4,for total cars 6 ")
 choice=int(input("                                                 selce the Car:"))
 
 shop(tax=0,vechile=0,motarcycle=0,cycle=0)
 if(choice==1):
   amount=int(input("Enter the amount(1000&):"))
   if(amount<1000):
     print("You cant bay Taxy")
     
   else:
     
     Total_taxy=Total_taxy=+1
     
     print("Total vechile %d"%Total_taxy)
     tax=+amount
     
     print("Your payed amount: %d"%tax)
 elif(choice==2):
   amount1=int(input("Enter the amount(4000&):"))
   if(amount1<4000):
     print("You can,t bay vechile")
     
   else:
     vechile=+amount1
     Total_vechile+=1
     print("Your Total Vechile :%d"%Total_vechile)
     print("Your payed amount : %d"%vechile)
 elif(choice==3):
   amount3=int(input("Enter the amount(200&):"))
   if(amount3<200):
     print("you cant bay motarcycle")
     
   else:
     motarcycle=+amount3
     Total_motarcycle+=1
     print("Your Total motarcycle:%d"%Total_motarcycle)

     print("Your payed amount :%d"%motarcycle)
 elif(choice==4):
   amount4=int(input("Enter the amount(100&):"))
   if(amount4<100):
     print("You can,t bay cycle")
   else:
     cycle=+amount4
     print("Your total cycle :%d"%Total_cycle)
     print("Your  payed amount:%d"%cycle)
 elif(choice==6):
    

  Total_cars(Total_cycle=0,Total_motarcycle=0,Total_taxy=0,Total_vechile=0) 
  print("Total cycle%d\n"%Total_cycle,'Total motarcycle %d\n'%Total_motarcycle,'Total taxy%d\n'%Total_taxy,"Totala vechile %d\n"%Total_vechile)      
 
 else:
   print("invilid choice")


