#Program to fix phone numbers during entry

def main():

    print()
    #Request input 
    phone = input("Paste phone number: ")

    #Remove obnoxious North American area code
    #Maybe should look into making the area code removable regardless of location
    entry = phone.removeprefix("+1").strip()

    #Removing parenthasis and adding dashes in correct spots
    entry = entry.replace("(", "-").replace(")", "-").strip("-")

    #This is for if they botched the parenthasis when typing
    #This is becoming a mess
    entry = entry.replace("- ", "-")
    
    #If decimal points were used, replace them with dashes
    entry = entry.replace(".", "-")
    
    
    #This needs to be at the end to check for double dashes
    entry = entry.replace("--", "-")
    
    #Print the completed result
    print()
    print(entry)
    print()


#Loop and Main
while True:
    main()
    if input("""Do you want to start again? (Y/N)""").strip().upper() != "Y":
        break
