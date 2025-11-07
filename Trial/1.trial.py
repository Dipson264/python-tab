def greet(name):
    return f"Hello, {name}!!!"


def sum(first, second):
    return first+second


def multiple(first, second):
    return first*second


def difference(first, second):
    return first-second


a = input("Enter your name:")
print(greet(a))

choice = int(input(
    "What do you want to do today? \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n"))


if choice == 1:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    result = sum(num_1, num_2)

elif choice == 2:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    result = difference(num_1, num_2)

elif choice == 3:
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    result = multiple(num_1, num_2)

else:
    print("Enter choice from 1-3.")
    exit()


print(f"The answer is {result}.")
