# labrary project




def show_Book(addotion_of_Book):
    return addotion_of_Book


def add_Book(add_Book):
    return add_Book


def tick_Book(tick_Book):
    return tick_Book





print("THis is the labrary of University ")
print("__________________________________________________________________________")
print("For show the Book prass 1:")
print("For add the Book prass 2:")
print("For the tick the Book  prass 3:")
num=int(input("select the labrary:"))

if(num==1):
    show_Book(addotion_of_Book=0)
    print(show_Book)
elif(num==2):
    add_Book(add_Book)
    show_Book+=add_Book
    print(show_Book)


elif(num==3):
    tick_Book(tick_Book)
    tick_Book-=show_Book
    print(tick_Book)
