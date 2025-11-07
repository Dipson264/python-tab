for x in range(10):
    for y in range(9):
        print(f"({x},{y})")


# for x in range(5):
#     for y in range(x):
#         print("*", end="")
#     print("\n")


row = int(input("Enter the no.of row:"))


for x in range(row+1):
    for y in range(x):
        print("X", end="")
    print("\n")
