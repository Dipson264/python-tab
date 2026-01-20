import math



result=False

def checker(Given_number):

    length = len(Number)
    integer_container = []
    for i in range(length):
        integer_container.append(int(Number[i]))

    powered_integer_container = []
    total_sum=0
    for i in range(length):
        powered_integer_container.append(math.pow(integer_container[i],length))
        total_sum+=powered_integer_container[i]

    print(total_sum)
    if total_sum==int(Number):
        return True
    else:
        return False

Number = input("Enter the number:")

result=checker(Number)

if result==True:
    print("The number is armstrong number.")
else:
    print("The number is not armstrong number.")



