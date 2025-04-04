import random

def num():
    """A program to guess Number between 0 and 99... """
    return random.randint(0 ,99)
def main():
    guess_num = num()
    while True:
        try:
            user_num=int(input("Enter a number"))
            # print(f"Think of a number between: {guess_num}")can check the number what is guessed8
            if user_num < 0 or user_num > 99:
                print("Please enter a number within the range 0-99.")

            if user_num <guess_num :
                print ("you guessed a low number")
            elif user_num > guess_num:    
                print (" you guessed a high number")
            else:
                print(f"Congratulations! your guess number {user_num} is correct")
                break
        except ValueError:
            print("enter correct value")
if __name__ == '__main__':
    main()
  
