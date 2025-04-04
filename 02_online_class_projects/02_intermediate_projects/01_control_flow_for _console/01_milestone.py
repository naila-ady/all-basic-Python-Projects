# import random
# rounds=5

# def num_gen(min=1, max=100):
#     """Generate a random number between 'min' and 'max'."""
#     return random.randint(min, max)

# def main():
#     score =0
#     for i in range(rounds):
#         print(f"rounds" ,{i +1})
#     # Generate random numbers for user and computer
#     user_num = num_gen()
#     comp_num = num_gen()
    
#     # Welcome message
#     print("Welcome to NailaAdnan GameZone!")
#     print("click to start the High-Low Game!")
#     print(f"Your number is: {user_num}")
    
#     # Ask the user to guess if their number is higher or lower than the computer's
#     print("Try to guess if your number is higher or lower than the computer's number!")
#     guess = input("Your guess ('higher' or 'lower'): ").strip().lower()
    
#     # Check if the user's guess is correct
#     if (guess == 'higher' and user_num > comp_num) or (guess == 'lower' and user_num < comp_num):
#         print(f"The computer's number was: {comp_num} and your number was {user_num} ")
#         score += 1
#         print("So it's Correct! You get a point!😊")
#         print("Have More Fun")
#     else:
#         print(f"The computer's number was: {comp_num} and your number was {user_num} ")
#         print("So it's Wrong! No point for you.😞")
#         print ("Better luck next time!")
#     print (f"your final score after round {i +1} is {score}")


# if __name__ == '__main__':
#     main()

import random

rounds = 5  # Total rounds to play

def num_gen(min=1, max=100):
    """Generate a random number between 'min' and 'max'."""
    return random.randint(min, max)

def main():
    score = 0  # Initialize score
    
    print("Welcome to NailaAdnan GameZone!")
    print("Click to start the High-Low Game!\n")
    
    for i in range(rounds):
        print(f"Round {i + 1}")  # Print the round number
        
        # Generate random numbers for user and computer
        user_num = num_gen()
        comp_num = num_gen()
        
        print(f"Your number is: {user_num}\n")
        
        print("Try to guess if your number is higher or lower than the computer's number!\n")
        guess = input("Your guess ('higher' or 'lower'): ").strip().lower()
        
        # Check if the user's guess is correct
        if (guess == 'higher' and user_num > comp_num) or (guess == 'lower' and user_num < comp_num):
            print(f"The computer's number was: {comp_num} and your number was {user_num}.\n")
            score += 1
            print("So it's Correct! You get a point! 😊\n")
        else:
            print(f"The computer's number was: {comp_num} and your number was {user_num}.\n")
            print("So it's Wrong! No point for you. 😞")
            
        
        print(f"Your score after round {i + 1} is {score}\n")
    
    # Final message after all rounds
    print(f"Game Over! Your final score is: {score}/{rounds}")
    if score == rounds:
        print("Wow! You played perfectly!")
    elif score > rounds // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

    
if __name__ == '__main__':
    main()
