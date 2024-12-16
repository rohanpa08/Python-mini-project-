#-------------mini project-------------------
#------------otp generator-----------------

import random

def generate_otp():
    # user  10-digit input
    user_input = input("Enter a 10-digit number: ")
    
    
    if len(user_input) == 10 and user_input.isdigit():
        random.seed(user_input) 
        otp = random.randint(0, 9999)  
        print(f"Your OTP is: {otp}")
    else:
        print("Invalid input! Please enter a valid 10-digit number.")

# Call the function
generate_otp()
