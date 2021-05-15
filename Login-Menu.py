print(" _   _  ___  _    ___  __   __ __  ___  _  _  _  ")
print("| | | || __|| |  / _/ /__\ |  V  || __|/ \/ \/ \ ")
print("| 'V' || _| | |_| \__| \/ || \_/ || _| \_/\_/\_/ ")
print("!_/ \_!|___||___|\__/ \__/ |_| |_||___|(_)(_)(_) ")
import os
decision = True
while decision:

    username =  input("Enter New Username: ")
    password = input ("Enter New Password: ")
    if len(username) >= 8:
        os.system('cls')
        print("Account Created!!!")
    else:
        os.system('cls')
        print("Account Not Created!!! The Program will now exit please press any key!!!")
    if len(username) >= 8 and len(password) >=8:
        usern = input("Enter Username: ")
        if len(usern) >= 8:
            if usern == username:
                y = input("Enter Password: ")
                if len(y) >= 8:

                    if y == password:
                        os.system('cls')
                        print("Login Success!!!")
                    else:
                        os.system('cls')
                        print("Login Failed")
                        break
                else:
                    os.system('cls')
                    print("Invalid Account Try Again!")
                    break
            else:
                os.system('cls')
                print("Incorrect User!")
                break
        else:
            os.system('cls')
            print("Insufficient Character!")
            break
    else:
        os.system('cls')
        print("Login Error!")
        break

    choice = input("Press [y] to continue or any key to exit: ")
    os.system('cls')
    decision = choice == "y" or choice == "Y"