quit_flag=True
is_started=False
while quit_flag:
    User_input = input(">")
    if User_input.upper() == 'HELP':
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit")
    elif User_input.upper()=='START':
        if is_started:
            print("Car is Already started!")
        else:
            print("Car Started...Ready to GO!")
            is_started = True
    elif User_input.upper()=='STOP':
        if is_started:
            print("Car Stopped.")
            is_started = False
        else:
            print("Car is not Started yet.")
    elif User_input.upper()=='QUIT':
        confirm=input("Do you really want to exit?(Y/N)  ")
        if confirm.upper()=="Y":
            quit_flag = False
        else:
            quit_flag = True
    else:
        print("I don't undertsande that...")
        quit_flag = True