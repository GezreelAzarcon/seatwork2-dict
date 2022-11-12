# Create a menu with 3 options
print("===================================================")
print("||                     MENU                      ||")
print("---------------------------------------------------")
print("||               Add an item --> 1               ||")
print("||           Search for an item --> 2            ||")
print("||               Exit Program --> 3              ||")
print("===================================================")

# create an empty main dictionary (Created dictionaries will be saved here)
alldict = {}

# Use While True here
while True:

    # Ask for user input on what to do
    menu = int(input("What do you want to do? "))
    
    # If 1, add
    if menu == 1:

        # Ask input for every personal data
        print(          "===================================================")
        username = input( "||What is your first name? ")
        fullname = input( "||What is your full name? ")
        age = int(input(  "||What is your age? "))
        address = input(  "||What is your address? ")
        phone_num = input("||What is your phone number? ")
        sick = input(     "||Are You sick? ")
        print(          "---------------------------------------------------")
        print(          "||      You have successfully added this user    ||")
        print(          "===================================================")
        
        # Append gathered input into the empty main dictionary
        alldict[username] = {
                            "Name": fullname,
                            "Age": age,   
                            "Address": address,
                            "Phone Number": phone_num,
                            "Sick": sick
                            }   
    
    # If 2, search
    if menu == 2:
        print(        "===================================================")
        who = input(  "||Who do you want to find? Enter First Name: ")
        print(        "===================================================")

        if who in alldict:
            print("||                 User Exists!                   ||")
            print( "---------------------------------------------------")
            print("||Name:", alldict[who]['Name'])
            print("||Age:", alldict[who]['Age'])
            print("||Address", alldict[who]['Address'])
            print("||Phone Number", alldict[who]['Phone Number'])
            print("||Sick", alldict[who]['Sick'])
            print( "===================================================")
        else:
            print( "===================================================")
            print("||              User doesn't exist!               ||")
            print( "===================================================")
        
    # If 3, ask if user wants to exit
    if menu == 3:

        # Create an input asking user if they want to quit
        print(         "===================================================")
        quitq = input( "||Do you want to quit? [y/n]: ")
        print(         "===================================================")

        # If yes, use break
        if quitq == 'y':
            break
        # else, continue
        else:
            continue    