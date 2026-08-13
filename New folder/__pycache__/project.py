
pass1=123
attempt=3
while True:
    pass1=int(input("enter the password:"))
    if(pass1==123):
        print("loug out")
        break
    else:
        attempt=attempt-1
        if(attempt>0):
            print("wornge password %d",attempt,"left")
            
        else:
            print("system close")
            break