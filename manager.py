
#You'll have to open this file and set the Master pass where 'Placeholder' is written because im currently trying to figure out how to save the master password as a file
print("Are you using this for the first time")

Y = "Y"
n = "N"
var1 = "T"
Expand
manager.py
4 KB
﻿
#You'll have to open this file and set the Master pass where 'Placeholder' is written because im currently trying to figure out how to save the master password as a file
print("Are you using this for the first time")

Y = "Y"
n = "N"
var1 = "T"
var2 = "I"
var3 = "R"
var4 = "G"

user = input('(' + Y + ')es ' +  ' (' + n + ')o ' )

if user == n:
  Masterpass = "Placeholder"
  if Masterpass == input("Please enter master password "):
    print("Logging in")
  
    print("Which password would you like to access")
    passwordtype = input('(' + var1 + ')witter ' + ' (' + var2 + ')nstagram ' + ' (' + var3 + ')eddit ' + ' (' + var4 + ')ithub ')
    if passwordtype == var1:
        file = open("Twittermail.txt", 'r') 
        datat1 = file.read()
        print("The mail id is " + datat1)
        file.close()
        file = open("Twitterpass.txt", 'r')
        datat2 = file.read()
        print("The password is " + datat2)
        file.close()
            
    elif passwordtype == var2:
           file = open("Instamail.txt", 'r')
           datai1 = file.read()
           print("The mail id is " + datai1)
           file.close()
           file = open("Instapass.txt", 'r')
           datai2 = file.read()
           print("The password is " + datai2)
           file.close()

    elif passwordtype == var3:
           file = open("Redditmail.txt", 'r')
           datar1 = file.read()
           print("The mail id is " + datar1)
           file.close()
           file = open("Redditpass.txt", 'r')
           datar2 = file.read()
           print("The password is " + datar2)
           file.close()
    
    elif passwordtype == var4 :
           file = open("Gitmail.txt", 'r')
           datag1 = file.read()
           print("The mail id is " + datag1)
           file.close()
           file = open("Gitpass.txt", 'r')
           datag2 = file.read()
           print("The Password is " + datag2)
           file.close()
    else:
           input("Invalid entry, Please try again " + " [Enter the letters present in the brackets]")
  else:
      print("Passwords do not match, please try again")


elif user == Y:
    print("Welcome to pypass manager by zuxarido :) ")
    print("Which password would you like to save")
    passtype = (input('(' + var1 + ')witter ' + ' (' + var2 + ')nstagram ' + ' (' + var3 + ')eddit ' + ' (' + var4 + ')ithub '))    
    
    if passtype == var1:       
        print("Do you want to generate a random password")
        randpassword = input('(' + Y + ')es ' + ' (' + n + ')o')
        if randpassword == Y:
            import random
            Capital_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            Small_letters = "abcdefghijklmnopqrstuvwxyz"
            numbers = "1234567890"
            punctuation = ",.?!"
            special_characters = "!@#$%&*()`~"
            length = int(input("Enter the length for password  "))
            password = ""

            for i in range(length+1):
                   password += random.choice(Capital_letters + Small_letters + numbers + punctuation + special_characters)
            print(password + "Please copy it and then enter it next")
            file = open("Twittermail.txt", 'w')
            passrand = input("Please enter the randomly generated password")
            file.write(passrand)
            file.close()

        elif randpassword == n:
            file = open("Twittermail.txt", 'w')
            passrand = input("Please enter a password")
            file.write(passrand)
            file.close()
