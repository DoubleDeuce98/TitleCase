#Program to fix phone numbers during entry

def main():

    print()
    #Request input 
    phone = input("Paste phone number: ")

    #Remove obnoxious North American area code
    #Maybe should look into making the area code removable regardless of location
    phone = phone.removeprefix("+1").strip()
    entry = phone.removeprefix("1-").strip()

    #Check if input was only digits and format
    if entry.isalnum():
        l = len(entry)
        print()

        if l == 11:
            print(l, "digits... Removing country code...")
            print("Please review output for errors:")
            print()
            entry = entry.removeprefix("1")
        
        elif l > 11:
            print("MORE DIGITS THAN EXPECTED, PLEASE REVIEW OUTPUT:")
            print()
    
    
        print(""+entry[:3]+"-"+entry[3:6]+"-"+entry[6:])
        print()

        return

    #Removing parenthasis and adding dashes in correct spots
    entry = entry.replace("(", "-").replace(")", "-")

    #This is for if they botched the parenthasis when typing
    #This is becoming a mess
    entry = entry.replace("- ", "-")
    
    #If decimal points were used, replace them with dashes
    entry = entry.replace(".", "-")

    #Remove spaces in between sets of numbers
    #Somehow forgot to do this forever ago...
    entry = entry.replace(" ", "-")
    
    #This needs to be at the end to check for double dashes
    entry = entry.replace("--", "-").strip("-")
    
    #Print the completed result
    print()
    print(entry)
    print()


#Loop and Main
print("PhoneFix")
print("Copyright (C) 2024 Theron Berg. All rights reserved.")

while True:
    main()
    if input("""Do you want to start again? (Y/N)""").strip().upper() == "N":
        break
