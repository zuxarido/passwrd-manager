# you'll have to open the python file to set the masterpass here becuase im currently trying to figure out how am i supossed to save it and stuff


masterpass = "placeholer"

G = "G"
S = 'S'
V = 'V'
Y = 'Y'
N = "N"
E = 'E'
G1 = "G"

print("Welcome to password manager by zuxarido :)")



print("What would you like to do ?")
task1 = input(
    '(' + G + ')enerate a random password ' + ' (' + S + ')ave a new password ' + ' (' + V + ')iew saved passwords ')

if task1 == G:
    import random

    Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    Small_letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "1234567890"
    punctuation = ",.?!"
    special_characters = "!@#$%&*()`~"
    length = int(input("Enter the length for password  "))
    password = ""

    for i in range(length + 1):
        password += random.choice(Capital_letters + Small_letters + numbers + punctuation + special_characters)
    print(password)
    print("Your password has been saved :)")
    procedure = input("(" + G1 + ')o back to the main menu ' + "(" + E + ')exit ')
    if procedure == E:
        print("Thank you for using password manager by zuxarido :) ")

    elif procedure == G1:
        print("still figuring this out")

    else:
        print("invalid entry, try again")

elif task1 == S:
    site = input("What would you like to associate this password with ? ")
    lid = input("Please enter login/mail id associated with " + site)
    file = open(site + "mail.txt", 'w')
    file.write(lid)
    file.close
    print("Would you like to generate a random password for this account? ")
    randpassword = input('(' + Y + ')es ' + ' (' + N + ')o ')
    if randpassword == Y:
        import random

        Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Small_letters = "abcdefghijklmnopqrstuvwxyz"
        numbers = "1234567890"
        punctuation = ",.?!"
        special_characters = "!@#$%&*()`~"
        length = int(input("Enter the length for password  "))
        password = ""

        for i in range(length + 1):
            password += random.choice(Capital_letters + Small_letters + numbers + punctuation + special_characters)
        print(password + "  This is the randomly generated password ")
        print("Would you like to use this password ")
        randpassworduse = input('(' + Y + ')es ' + ' (' + N + ')o ')

        if randpassworduse == Y:
            file = open(site + "pass.txt", 'w')
            file.write(password)
            file.close()
            print("Your password has been saved :) ")

        elif randpassworduse == N:
            pass1 = input("please enter the password you'd like to associate with this account ")
            file = open(site + "pass.txt", 'w')
            file.write(pass1)
            file.close()
            print("Your password has been saved :)")
            procedure = input("(" + G1 + ')o back to the main menu ' + "(" + E + ')exit ')
            if procedure == E:
                print("Thank you for using password manager by zuxarido :) ")

            elif procedure == G1:
                print("still figuring this out")

            else:
                print("invalid entry, try again")

    elif randpassword == N:
        pass1 = input("Please enter the password you'd like to associate with this account ")
        file = open(site + "pass.txt", 'w')
        file.write(pass1)
        file.close()
        print("Your password has been saved :)")
        print("What would you like to do now ?")
        procedure = input("(" + G1 + ')o back to the main menu ' + "(" + E + ')exit ')
        if procedure == E:
            print("Thank you for using password manager by zuxarido :) ")

        elif procedure == G1:
            print("still figuring this out")

        else:
            print("invalid entry , try again")

elif task1 == V:
    passid = input("Please enter the platform whose credential you'd like to access")
    file = open(passid + "mail.txt", 'r')
    mailid = file.read()
    print("The login id associated with " + passid + " is " + mailid)
    file.close()
    file = open(passid + "pass.txt", 'r')
    pass2 = file.read()
    print("The password for " + passid + " is " + pass2)
    print("What would you like to do now ?")
    procedure = input("(" + G1 + ')o back to the main menu ' + "(" + E + ')exit ')
    if procedure == E:
        print("Thank you for using password manager by zuxarido :) ")

    elif procedure == G1:
        print("still figuring this out")

    else:
        print("invalid entry , try again")


else:
    print("invalid entry, try again")






