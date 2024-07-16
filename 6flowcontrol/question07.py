def what_is_number(number):
    if number>=0 and number<=50:
        print(str(number) + " is between 0 and 50")
    elif number>=51 and number<=100:
        print(str(number) + " is between 51 and 100")
    elif number>100:
        print(str(number) + " is greater than 100")
    else:
        print(str(number) + " is less than 0")
        
what_is_number(-1)
what_is_number(25)
what_is_number(75)
what_is_number(100)
what_is_number(101)