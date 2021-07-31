from users import Users

loged_user = Users("harshit","harshit",["admin"],"system")
system_users = [loged_user]


def rbac(loged_user,system_users):
    while True:
        print(loged_user.uname + " you are logged in as " +  loged_user.roles[0].name + "\n")
        print("Enter 1 to create user")
        print("Enter 2 to delete a user")
        print("Enter 3 to login to another user ")
        print("Enter 4 to edit role of a user")
        print("Enter 5 to close")
        inp = str(raw_input())
        if inp == "1":
            uname = str(raw_input("Enter username : "))
            password = str(raw_input("Enter password : "))
            role = str(raw_input("Enter Role : "))
            resources = str(raw_input("Enter resourses space separated : ")).split(' ')
            user = Users(uname,password,[role],resources)
            system_users.append(user)
            print(uname + " is " + "created \n")
        elif inp == "2":
            if loged_user.roles[0].name == "admin":
                uname = str(raw_input("Enter username of the user you want to delete : "))
                nsu = []
                for su in system_users:
                    if su.uname == uname:
                        pass
                    else:
                        nsu.append(su)
                system_users = nsu
                print("user deleted \n")
            else:
                print("You do not have permission try again with admin user \n")
        elif inp == "3":
            uname = str(raw_input("Enter username : "))
            password = str(raw_input("Enter password: "))
            isf = False
            for su in system_users:
                if su.uname == uname and su.password == password:
                    loged_user = su
                    isf = True
                else:
                    pass
            if isf == False:
                print("User does not exists \n")
        elif inp == "4":
            if loged_user.roles[0].name == 'admin':
                uname = str(raw_input("Enter username : " ))
                password = str(raw_input("Enter password : "))
                role = str(raw_input("Enter Role : "))
                for su in system_users:
                    if su.uname == uname and su.password == password:
                        su.roles[0].name = role
                    else:
                        pass
            else:
                print("You do not have permission try again with admin user \n")
        elif inp == "5":
            break
        else:
            print("Invalid option try again \n")

rbac(loged_user,system_users)