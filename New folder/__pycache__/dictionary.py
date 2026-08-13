
def dictionary(english_to_englist):
    print("WELCOME TO ENGLISH DICTTIONARY")

english_to_englist={
    "walk":'to move'
    ,"king":'empiror'
    ,'car':"vechile"
    ,'fear':"threaten"
    ,"baby":"kid"
    ,"backup":'support'
    ,'ban':'prohibit'
    ,'bark':"yap"
    ,'base':'main part'
    ,'battle':'war'
    ,'animal':"beat"
} 

while True:
    num=input("Enter the word:")
    if(num in english_to_englist):
        print(num for num in english_to_englist.get(num))
