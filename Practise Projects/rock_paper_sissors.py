import random

play=['sissor','paper','rock']
machine_choice= random.choice(play)

def checker(m_choice,u_choice):
    if m_choice=="sissor" and u_choice=="sissor":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. The game is draw")
    elif m_choice=="paper" and u_choice=="paper":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. The game is draw")
    elif m_choice=="rock" and u_choice=="rock":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. The game is draw")
    elif m_choice=="rock" and u_choice=="paper":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. You win.")
    elif m_choice=="rock" and u_choice=="sissor":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. You lose.")
    elif m_choice=="paper" and u_choice=="rock":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. You lose.")
    elif m_choice=="paper" and u_choice=="sissor":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. You win.")
    elif m_choice=="sissor" and u_choice=="rock":
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. Your win.")
    else: 
        print(f"The machine choosed {m_choice} and you choosed {u_choice}. You lose.")
   
def choice():
    input_val=int(input(" 1.Sissor \n 2.Paper \n 3.Rock \n Enter your choice: \n "))
    # print(type(input_val),input_val)
    
    if input_val<=3 and input_val>=1:
       
        User_choice = play[input_val-1]
        checker(machine_choice,User_choice)

    else:
        print("Enter the value from 1-3.")
        choice()
        

    
choice()

