# simple code
# name = input("Please type your name and press enter. ")
# age = input("Please type  your age and press enter. ")
# game = input("Please type your favourite game and press enter. ")
# sentence = f"My name is {name}, I am {age} years old and my favourite game is {game} !"
# print(sentence)

# with function
begining_sentence="I mastered AI,and now my"
def main():
    """ a program which prompts the user for an adjective, then a noun, then a verb, 
    and then prints a fun sentence with those words!
    e.g:I mastered AI, and now (my) (new Laptop) refuse to start unless I (compliment its code)."""
    
adjective:str=input("Enter an adjective of your choice:")
noun:str=input("Enter a noun of your choice:")
verb:str=input("Enter a verb of your choice:")
print(f"{begining_sentence} {noun} {adjective} refuses to start unless I {verb}.")

if __name__ =='__main__':
    main()
