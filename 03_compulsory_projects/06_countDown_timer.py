# import time
# my_times=int(input("Enter time in seconds: "))
# # for i in range(0,my_times):for forward counting
# for i  in range(my_times ,0 ,-1):
#     seconds = i % 60
#     minutes =int(i / 60) % 60
#     hours=int(i /3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("It's time up")

import time

def countdown(t):
    print ("CountDown Starts")
    while t:
        mins, secs = divmod(t, 60)  # Calculate minutes and seconds
        timer = "{:02d}:{:02d}".format(mins, secs)  # Format the time
        print(f" {mins:02d}:{secs:02d}") 
        time.sleep(1)  # Wait for 1 second
        t -= 1  # Decrease the time by 1 second
    
    print("It's time up!")

# Get input from the user and start the countdown
try:
    t = int(input("Enter the time in seconds: "))
    countdown(t)
except ValueError:
    print("Please enter a valid number.")
