account_number = int(input("enter a account number"))
pin = int(input("enter a pin number"))
if account_number==123456 and pin == 0000:
    print("account number is valid")
    print("select 2 to balance enqiry,4 to withdraw")
    select = int(input("select 2 or 4"))
    if select == 4:
        print("you have selected a withdraw")
        withdraw = float(input("enter a amount value"))
        if withdraw <= 10000:
            print("transition is completed")
        else:
            print("insufficient fund")

        if select == 2:
            print("u have selected balance enqiry")
        elif():
            print("data is invalid please select 1 or 2")
        else:
            print("enter valid AC.number and pin")
