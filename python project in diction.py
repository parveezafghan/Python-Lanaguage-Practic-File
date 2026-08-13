

menus={"kabuly Falow":100,"Kabab":200,"ckecken":300}


print("Welcome to your resturen")
print("-----------------------------------------------")
print("kabuly Falow [1000]\n kabab [200]\n checken [300]")

select=(input("Select the food:"))

if(select in menus):
    Total=menus[select]
    print("Your Total amount is:%d"%Total)
   # print("are your want to another item yes,no")
    select1=input("are your want to another item yes,no")
    if(select1=="yes"):
        another_order=input("Select the food")
        Total=menus[another_order]
        print("your Total amount is:%d"%Total)
    else:
        print("think you")

else:
    print("invilide choice")


