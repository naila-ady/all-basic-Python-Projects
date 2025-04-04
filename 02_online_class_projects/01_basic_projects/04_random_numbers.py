# this ist code will generate a lst of number bcz we return it in a [list]
# import random

# def random_num(num, min_value=1, max_value=100):
#     """ A program to generate a list of 'num' random numbers in the given range."""
#     return [random.randint(min_value, max_value)for i in range(num)]

# def main():
#     num = 10  # Number of random numbers to generate
#     # for i in range(num):if want every number in a single list
#     random_numbers = random_num(num)
#     print(random_numbers)

# if __name__ == '__main__':
#     main()

# this second code will generate one number at a time
import random

def ran_num(min=1,max=100):
    return random.randint(min ,max)
def main():
    num=10
    for i in range(num):
        r=ran_num()
        print(r)
if __name__ == '__main__':
    main()

    
   