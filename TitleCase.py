#Program to lowercase dealer entry of addresses and other text

def main():
    #Request input 
    dealer = input("Paste line: ")

    #Title-ize the line the dealer provided
    entry = dealer.title()

    #Check if the title worked for the line or errored
    if entry.islower:
        print(entry)

    else: print("ERROR: Please notify Theron if time allows")
    
#Loop and Main
while True:
    main()
    if input("""Go again? (Y/N)""").strip().upper() != "Y":
        break
