information={}
emp_number=int(input("Enter the number of employee: "))

for i in range(emp_number):
    print(f"Iteration {i+1}")
    information.update({input("Enter the Name:"):input("Enter the key:")})
    # information[name] = password [Alternate way]
    

names = list(information.keys())
name_pass = list(information.values())


login_user=input("Enter your name:")
login_pass=input("Enther you pass:")

test_user=names[0]
for i in range(len(names)):
    if test_user==login_user:
        User_found=True
        found_location=int(i)
    else:
        User_found=False

# print(User_found)

if User_found:
    if name_pass[found_location]==login_pass:
        print("Logged in sucessfully.")
    else:
        print("Login failed. Incorrect Passoword")
else:
    print("No user found.")

