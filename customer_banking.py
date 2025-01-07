# Import the create_cd_account and create_savings_account functions
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("Please enter savings account balance: "))
    savings_interest = float(input("Please enter savings account interest rate as a percentage: "))
    savings_maturity = int(input("Please enter number of months for savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

     # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nSavings Account Summary:")
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nPlease enter CD account balance: "))
    cd_interest = float(input("Please enter CD account interest rate as a percentage: "))
    cd_maturity = int(input("Please input number of months for CD account: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.