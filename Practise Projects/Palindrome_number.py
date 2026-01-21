def is_palindrome(check_val):
    reversed_val= check_val[::-1] #Reverses the string
    return check_val==reversed_val


number=input("Enter the number that you want to check if it's palindrome number or not: ")

if is_palindrome(number): #If true
    print("The number is palindrome number.")
else: 
    print("The number is not palindrome number.")