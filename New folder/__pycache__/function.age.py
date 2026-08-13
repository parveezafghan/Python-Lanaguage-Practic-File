while True:
 first_name=input("Enter first name:")
 second_name=input("Enter second name:")

 birth_date=int(input("Enter birth date:"))
 current_date=int(input("Enter current date:"))



 def full_name(first_name,second_name):
    
    return first_name,second_name
    






 def full_age(birth_date,current_date,date):
    date=birth_date-current_date
    return date




 x,y=full_name(first_name,second_name)

 print(x,y)

 date=full_age(birth_date,current_date,date=0)


 print(date)


























'''
get_user_detials1=input("Enter  first name:")
get_user_detials2=input("Enter second name")
get_user_detials3=int(input("Enter birth Date:"))
get_user_detials4=int(input("Enter current:"))

def full_name(first_name,last_name,name):
    name=first_name+last_name
    return name


def  full_date(birth_date,current_date):
    date=birth_date-current_date
    return date


name=full_name((get_user_detials1,get_user_detials2,))
print(f"{name}")

date=full_date(get_user_detials3,get_user_detials4)
print(f"{date}")

'''