# Create a menu with 3 options
print("=================================")
print("||            MENU             ||")
print("---------------------------------")
print("||       Add an item --> 1     ||")
print("||   Search for an item --> 2  ||")
print("||      Exit Program --> 3     ||")
print("=================================")

# create an empty main dictionary (Created dictionaries will be saved here)
alldict = {}

# Use While True here
while True:

    # Ask for user input on what to do
    menu = int(input("What do you want to do? "))
    
    # If 1, add
    if menu == 1:

        # Ask input for every personal data
        username = input("What is your name? ")
        age = int(input("What is your age? "))
        address = input("What is your address? ")
        phone_num = input("What is your phone number? ")
        print("You have successfully added this user")

        # Append gathered input into the empty main dictionary
        alldict[username] = {
                            "Name": username,
                            "Age": age,   
                            "Address": address,
                            "Phone Number": phone_num
                            }
    print(alldict)     
    # If 2, search
    if menu == 2:
        who = input("Who do you want to find? Enter First Name: ")
        if who in alldict:
            print("User Exists!")
            print("Name:", alldict[who]['Name'])
            print("Age:", alldict[who]['Age'])
            print("Address", alldict[who]['Address'])
            print("Phone Number", alldict[who]['Phone Number'])
        else:
            print("User doesnt exist!")
        
    
        # Use input to check if the dict user wants exists
        # If exists, print the dictionary using for loop
        # If not Continue
    # If 3, ask if user wants to exit
        # Create an input asking user if they want to quit
    if menu == 3:
        quitq = input("Do you want to quit? [y/n] ")
                # If yes, use break
        if quitq == 'y':
            break
            # else, continue