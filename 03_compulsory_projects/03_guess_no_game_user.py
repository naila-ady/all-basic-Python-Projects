import random
def number_guess():
    """ Take input from user and guess a number  """
    user_guess = 0
    guess_number = random.randint(1, 100)
    while guess_number != user_guess:
        user_guess = int(input("Enter a number(1,100)"))
        if  user_guess > guess_number:
            print("Sorry try one more time.Your guess is too high")
        elif  user_guess < guess_number:
            print("Sorry try one more time.Your guess is two low")
        else:
            print(f"Congratulations! {guess_number} is a correct guess")
number_guess()   
        
    
