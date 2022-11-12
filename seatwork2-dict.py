# Create a menu with 3 options
print("=================================")
print("||            MENU             ||")
print("---------------------------------")
print("||       Add an item --> 1     ||")
print("||   Search for an item --> 2  ||")
print("||      Exit Program --> 3     ||")
print("=================================")

count = 0

# create an empty list (Created dictionaries will be saved here)
userlist = []

# Use While True here
while True:

    # Ask for user input on what to do
    menu = int(input("What do you want to do? "))
    
    # If 1, add
    if menu == 1:
        
        # Create an empty dictionary variable (ask user for input on variable name)
        count += 1
        usernum = "User"+str(count) 

        # Ask input for every personal data
        name = input("What is your name? ")
        age = int(input("What is your age? "))
        address = input("What is your address? ")
        phone_num = input("What is your phone number? ")

        # Append gathered input into the empty dictionary
        # Append the new dictionary into the empty list
        userlist.append({usernum:
                            {"Name": name,
                             "Age": age,   
                             "Address": address,
                             "Phone Number": phone_num
                            }     
                        })
        print(userlist[:]['User']['Name'])
    # If 2, search
        # Use input to check if the dict user wants exists
        # If exists, print the dictionary using for loop
        # If not Continue
    # If 3, ask if user wants to exit
        # Create an input asking user if they want to quit
            # If yes, use break
            # else, continue