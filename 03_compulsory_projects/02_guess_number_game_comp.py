import random

def computer_guess():
    """ A program to verify the number guessd by computer ,it will not stop
    untill receives correct"""
    low = 1
    high = 100
    feedback = ''
    
    print("Think of a number between 1 and 100 and I'll try to guess it!")

    while feedback != 'c':
        if low > high:
            print("Wait a second... Something's not right! 🤔")
            break

        guess = random.randint(low, high)
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f"Yay! I guessed your number: {guess} 🎉")
        else:
            print("Please enter H, L, or C only.")

computer_guess()
