def check_loan_eligibility():
    # Input customer details
    try:
        salary = float(input("Enter your monthly salary: "))
        loan_amount = float(input("Enter the loan amount requested: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for salary and loan amount.")
        return

    # Eligibility conditions
    if salary < 30000.00:
        print("Loan not approved: Your salary is below the minimum requirement of 30,000.00.")
    elif loan_amount > 10 * salary:
        print("Loan not approved: The requested loan amount exceeds 10 times your monthly salary.")
    else:
        # Customer is eligible
        months = int(input("Enter the number of months to pay back the loan: "))
        total_loan_with_interest = loan_amount * 1.10  # 10% interest increase
        monthly_payment = total_loan_with_interest / months

        print(f"Congratulations! You are approved for the loan.")
        print(f"Total amount to be repaid (with interest): {total_loan_with_interest:.2f}")
        print(f"Your monthly payment over {months} months will be: {monthly_payment:.2f}")

# Run the program
check_loan_eligibility()
