

users = ["Ansuya", "Dipson", "Aayam", "Anish", "Yathartha",
         "Arya", "Ricky", "Riya", "Reetisha", "Santosh"]
pass_key = [7422, 2564, 5512, 7712, 4545, 7124, 5151, 9841, 7162, 5050]

user_name = input("Enter your username:")
pass_word = int(input("Enter your pin: "))
userfound = False
x = 0
found = False
while x < len(users):
    test = users[x]
    if user_name == test:
        pin = pass_word
        if pass_key[x] == pin:
            print(f"Sucessfully loged into {user_name}.")
            userfound = True
        else:
            print("The pin is incorrect.")

    x += 1

if not userfound:
    print("The user is not found.")
