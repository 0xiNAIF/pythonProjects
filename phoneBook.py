# Ask the user search by name or number
print("[+] Choose Number:\n")
print("[1] Search By Number")
print("[2] Search By Name")
print("[3] List Names Available")

choosen = int(input('=> '))

# Check what user entered, then execute desired way

if choosen == 1:
    number = int(input("Enter a Number: "))
    countNumber = countDigits(number)
    # check whether 10 digits entered or not
    if (countNumber == 10):
        # Grab the name of the entered number
        for name in phoneBook:
            if (phoneBook[name] == number):
                print(f"The phone number {number} belongs to => {name}")
    else:
        print("Invalid number")

elif choosen == 2:
    name = input("Enter the name (Case Sensitive): ")
    for i in phoneBook:
        if (name == i):
            print(f"The number is => {phoneBook[i]} ")

elif choosen == 3:
    for i in phoneBook:
        print(i)


else:
    print("Have you choosen a right number ?")
