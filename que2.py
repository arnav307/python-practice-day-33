def division():
    try:
        user1=int(input("enter a first number: "))
        user2=int(input("enter a second number: "))
        division=user1/user2  
        print(f"The division of two number is {division}")
    except ZeroDivisionError:
        print("Please enter any number expect zero!!!")
    except ValueError:
        print("please enter a integer not string!!!!!")
division()