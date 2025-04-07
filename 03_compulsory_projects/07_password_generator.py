import random
def main():
    alphabets="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?01234567890"
    len=int(input("Enter the length of password"))
    num=int(input("Enter the number of password"))
    print("Here are your passwords:")
    for abc in range(num):
        password = ""
        for i in range(len):
            password += random.choice(alphabets)
        print(password)
if __name__ == '__main__':
    main()   
    
    
    