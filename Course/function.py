def add(first_num, second_num):
    sum = first_num+second_num
    return sum


a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
answer = add(a, b)
print(f"The sum of the two numbers are:{answer}")
