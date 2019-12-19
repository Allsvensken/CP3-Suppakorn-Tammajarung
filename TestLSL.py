username = input("Username : ")
password = input("Password : ")
if username == "allsvensken" and password == "suppabas25":
    print("Welcome ! ")
    print("1.list 1 , price : 50 THB")
    print("2.list 2 , price : 30 THB")
    print("3.list 3 , price : 20 THB")
    print("4.list 4 , price : 35 THB")
    userselected = int(input(">>>"))
    if userselected == 1:
        print("success")
        price = 50
        number = int(input("How many pieces do you want ? : "))
        print("Total price = ", number * price)
    elif userselected == 2:
        price = 30
        number = int(input("How many pieces do you want ? : "))
        print("Total price = ", number*price)
    elif userselected == 3:
        price = 20
        number = int(input("How many pieces do you want ? : "))
        print("Total price = ", number*price)
    elif userselected == 4:
        price = 35
        number = int(input("How many pieces do you want ? : "))
        print("Total price = ", number*price)



