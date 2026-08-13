
#list project in python
list=['mouse','computer','cable','manator','computer','mouse','speter','mouse']


#first fuction
def serch():
    list=input("Enter the items:")
    print("your times",list,list.count(list),'left in stoke')
#second function
def sell():
    sell=input("Enter the items:")
    sell.remove(list)

#third function

def add():
    add=input("Enter the items:")
    list.insert(0,add)

while True:
    print("Welcome to khan store")
    print("select the operation:")
    print("for serching =s:")
    print("for sell=c:")
    print("for adding =a:")

    operation=input("choice the operation:")
    if(operation=="s"):
        serch()
    elif(operation=="c"):
        sell()
    elif(operation=='a'):
        add()

