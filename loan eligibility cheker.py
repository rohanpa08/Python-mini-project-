#-----------------------MINI PROJECT----------------------: 
#-------------Simple Loan Eligibility Checker-----------------

# --------Taking user's income and credit score as input
income = float(input("Enter your monthly income: ₹ "))
credit_score =int( input("Enter your credit score: "))

#the income is grether than input income and credit score is match then eligible
if income >= 30000 and credit_score >= 700:
        print("Congratulations! You are eligible for the loan.")
elif income >= 25000 and credit_score >= 650:
        print("You are eligible for the loan with conditions. Please review your terms.")
else:
        print("Sorry, you are not eligible for the loan based on the given details.")