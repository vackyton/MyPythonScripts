#   Welcome! Today this will teach you if statements!
#   We will first make a password
#   Made by Vackyton
Password1 = input(" Enter the password to access files : ")
if Password1 == "Wackyness":
    print("Vackyton likes Computers And Coding!")
#   Remember to make sure there is a space between the start of the line or it will not work
#   This statement makes sure the password is right!Make sure it is lowercase or it will need to
#   be perfect caps for ex:wackyness will return "Lolno" unless it is "Wackyness"
elif Password1 == "NoWack":
    print("Fine you got me")
    #elif statements mean else if and can be used forever!
elif Password1 == "FREEKEY":
    print("REEEEEEEEEE HOW DID U KNOW")
else:
    print("Wrong password access denied :)")
    
#   The else statement does what it means. If the password is not "Wackyness" It will run the else statement,
#   you can make a another password
#   So know you know how to make a password!
