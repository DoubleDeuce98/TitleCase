#Program to lowercase dealer entry of addresses and other text

def main():

    print()
    #Request input 
    dealer = input("Paste line: ")

    #Title-ize the line the dealer provided
    entry = dealer.title()

    #Check if the title worked for the line or errored
    if entry.islower:
        print("")
        print(entry)
        print("")

    else: print("ERROR: Please send a screenshot of the terminal to theronberg@columbiacabinets.com")
    
#Loop and Main
while True:
    main()
    if input("""Do you want to start again? (Y/N)""").strip().upper() != "Y":
        break
