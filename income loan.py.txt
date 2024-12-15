#------------ Mini Project--------------: 
#-------------Simple Loan Eligibility Checker-----------------

# --------Taking user's income and credit score as input
income = input("Enter your monthly income: ₹ ")
credit_score = input("Enter your credit score: ")


if income.isdigit() and credit_score.isdigit():
    income = float(income)  
    credit_score = int(credit_score)  


    if income >= 3000 and credit_score >= 700:
        print("Congratulations! You are eligible for the loan.")
    elif income >= 2500 and credit_score >= 650:
        print("You are eligible for the loan with conditions. Please review your terms.")
    else:
        print("Sorry, you are not eligible for the loan based on the given details.")
else:
    print("Invalid input! Please enter valid numerical values.")
