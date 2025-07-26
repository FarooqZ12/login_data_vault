login_infos = []

while True:  # This statement will run the loop. when operation performe.
    print("What do you want to do?")
    print("1. Add a new login info")
    print("2. View all login info")
    print("3. Delete a login")
    print("4. Exit")

    operation = int(input("What you want? (1,2,3,4) "))  # input from user

    if (operation == 1):  # Add new login
        website = input("what is website name? ")
        username = input("Username: ")
        password = input("Password: ")
        login_info = (website, username, password)
        login_infos.append(login_info)

        print("Login info Saved")

    elif (operation == 2):  # print all login info
        if len(login_infos) == 0:
            print("No data stored yet!")
        else:
            for w, u, p in login_infos:
                print("Website:", w, "|""Username:", u, "|""Password:", p)

    elif (operation == 3):  # remove complete meal
        login_infos.clear()
        print("complete  removed.")

    elif (operation == 4):  # this will end the the process
        print("Good by")
        break

    else:
        print("Invalid input. Please enter (1,2,3,4): ")
