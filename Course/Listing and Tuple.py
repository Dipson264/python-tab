user_names = ["Dipson", " Ayam", "Ansuya",
              "Arya", "Riya", " Reetisha", " Anish"]
name = input("Enter your name: ")
x = 0
while x < len(user_names):
    trial = user_names[x]
    if trial == name:
        print(f"The username is found, User found in {x+1} trial. ")
        exit()
    x += 1

print("User is not found.")
