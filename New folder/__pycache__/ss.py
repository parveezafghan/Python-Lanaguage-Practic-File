import time
'''
def red_light():
    print("stop red light")
    time.sleep(3)

def yellow_light():
    print('redy to move')
    time.sleep(3)

def green_light():
    print("GO")
    time.sleep(3)

def traffic_system():
    while True:
        red_light()
        yellow_light()
        green_light()
    


traffic_system()



pass1="afghan123"
attempt=3
while  attempt>0:
    pass1=input("enter the password")
    if(pass1=='afghan123'):
        print("correct password")
        break
    

    else:
        attempt-=1
        if(attempt>0):
          print(f"remind change:{attempt}")

'''

pass1="afghan"
attempt=3
while attempt>0:
 pass1=(input("enter password"))
 
if(pass1=="afghan"):
    print("it is correct")
    
else:
   attempt-3
   if(attempt>0):
      print(f"remind chance{attempt}")


    

pass1()

                
                
        


    '''
while True:
 name=input("Enter your name:")

 wifi=int(input("Enter wifi passwod:"))

 wifi1=(input("Enter second passwod"))
 if(name=='parveez' and (wifi==123 or wifi1==50)):
  print("welcome to system")
 else:
  print("Try again")

attempt=3

while True:
  
  num_password=int(input("Enter the password in number:"))
  al_password=input("Enter the pssword in strange:")
  if(num_password==123 and al_password=='king'):
    print("Welcome to system")
    break
  else:
    attempt-=1
    print("your attempt %d"% attempt,"left")
    if(attempt==0):
      print("system off")
      break
'''
