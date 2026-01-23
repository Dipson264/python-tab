'''def great(num_1=0,num_2=0,num_3=0):
    if num_1>num_2 and num_1>num_3:
        return print(f"{num_1} is the greatest among the three numbers.")
    elif num_2>num_1 and num_2>num_3:
        return print(f"{num_2} is the greatest among the three numbers.")
    else:
        return print(f"{num_3} is the greatest among the three numbers.")

def fahren_conv(c_val=0):
    return print((c_val *9/5)+32)

def n_sum(n):
    if (n==1):
        return 1
    return n_sum(n-1) + n

great(2,6,7)
fahren_conv(25)
print("hi", end="") 
print(n_sum(4))'''


def pattern_printer(n):
    i=0
    j=0
    
    while (i<n):
        while (j<i):
            print("*",end="")
            j+=1
        print("\n")
        i+=1
    


pattern_printer(3)