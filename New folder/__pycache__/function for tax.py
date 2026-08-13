tax=0
while True:
    name=input("Enter your full name:")
    salary=int(input("Enter your salary:"))


    def full_name(name):
        return name
    

    def amount(salary,tax):
        if salary<=2000:
            return print(f"{salary}your don,t have tax to  pay")
        elif salary>=5000:
            tax=salary-200
            return print(f"your total tax{tax} in {salary}  ",tax)
        elif salary>=10000:
            tax=salary-500
            return print(f'your total tax {tax}in ',salary)
        elif salary>=20000:
            tax=salary-1500
            return print(f"your total tax {tax} in ",salary)
        elif salary>=50000:
            tax=salary-3000
            return print(f'your total {tax} in ')
        






    name=full_name(name)
    print(f"your name is {name}")
    amount(salary,tax)
    print()
        

        


