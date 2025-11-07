income = int(input("Enter your annual income:"))
credit = int(input("Enter your credit score:"))
student = str(input("Are you a student?(Y/N):"))


if student.capitalize() == "Y":
    student_condition = True
elif student.capitalize() == "N":
    student_condition = False
else:
    print("Enter either Y or N.")


if income > 500000:
    income_lvl = True
else:
    income_lvl = False

if credit > 5:
    credit_lvl = True
else:
    credit_lvl = False


if (income_lvl or credit_lvl) and student_condition:
    print("You are eligible for the loan")
else:
    print("You are not eligible for loan")
