"""
    Author : naif alghamdi
    Description : 
    This simple phone book program is exersice about control-flow in python
    it searches using a number or name
    twitter:
    @naif707x

    Note :
    Feel free to improve the code :)

"""

phoneBook = {
    "Amal": 1111111111, "Mohammed": 2222222222, "Khadijah": 3333333333,
    "Abdullah": 4444444444, "Rawan": 5555555555, "Faisal": 6666666666,
    "Layla": 7777777777
}

# Function that count number of digits for phone number


def countDigits(num):
    count = 0
    while num != 0:
        num //= 10
        count += 1
    return count


choosen = None
while choosen != 0:
    # Ask the user search by name or number
    print("[+] Choose Number:\n")
    print("[1] Search By Number")
    print("[2] Search By Name")
    print("[3] List Names Available")
    print("\n Type 0 to leave the program")

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
