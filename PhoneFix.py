#Program to fix phone numbers during entry

def main():

    print()
    #Request input 
    phone = input("Paste phone number: ")

    #Remove obnoxious North American area code
    #Maybe should look into making the area code removable regardless of location
    entry = phone.removeprefix("+1")

    #Removing whitespace and adding dashes in correct spots
    entry = entry.replace("(", "").replace(") ", "-").strip()

    print()
    print(entry)
    print()


#Loop and Main
while True:
    main()
    if input("""Do you want to start again? (Y/N)""").strip().upper() != "Y":
        break
