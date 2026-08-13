
store_add_list=[]
selling_things=[]

def add_thing():
    things=input("Enter the things To add the store:")
    store_add_list.append(things)



def  serch_item():
    serch=input("Enter the things Your want TO serch:")
    print(store_add_list.count(serch))


def delele_Record():
    delect=input("Enter the things You want To delect:")
    del store_add_list[delect]


def Clear_stor():
    store_add_list.clear()


def show_stor():

    for show in store_add_list:


        print(show)

def sell_things():
    sell=input("which things Your want TO bay:")
    store_add_list.remove(sell)
    selling_things.append(sell)

    

while(1):
    print("1.For add 2.for serch  3. For Delele 4.Clear system 5.show stor 6.for sell 7.for selling thins")
    print("select the operation:")
    select=int(input("Select :"))
    if(select==1):
        add_thing()
    elif(select==2):
        serch_item()
    elif(select==3):
        delele_Record()
    elif(select==4):
        Clear_stor()
    elif(select==5):
        show_stor()
    elif(select==6):
        sell_things()
    elif(select==7):
        print(selling_things)
        

    
