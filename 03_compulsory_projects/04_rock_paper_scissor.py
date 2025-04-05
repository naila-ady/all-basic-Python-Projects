import random  
def rock_paper_scissor():
    options=["rock" ,"paper","scissor"]
    computer_choice=random.choice(options)
    user_choice=input("Enter your choice:(options)\n").strip().lower()
    if user_choice not in options:
        print("Invalid choice! Please try again.")
        return
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print ("It's a Tie")
    elif (user_choice == "rock" and computer_choice == "scissor")or \
         (user_choice == "paper" and computer_choice == "rock")or \
         (user_choice == "scissor" and computer_choice == "paper"):
        print ("🏆 you Win")
    else:
        print("You lose! 😢")

rock_paper_scissor()

 
 
 
