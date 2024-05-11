def prompt(message):
    '''
    prepend the marker to the front of each output string we pass to print
    '''
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        number = float(number_str)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True

    return False

def invalid_interest(number_str):
    '''
    for checking if interest rate is valid.  
    to avoid user unintentionally enter a decimal value.  
    prompt user to confirm when user input is les than 1
    '''
    try:
        number = float(number_str)
        if number < 0:
            raise ValueError
        if number < 1:
            prompt(f'You have entered {number}%, to confirm please enter "y"')
            confirmation = input().lower()
            if confirmation.startswith('y'):
                return False
            raise ValueError
    except ValueError:
        return True

    return False

prompt("Welcome to Mortgage Calculator!")

while True:
    prompt("---------------------------------")

    # prompt user to enter the loan amount and check if the input is valid
    prompt('What is your loan ammount') 
    loan_amount = input()

    while invalid_number(loan_amount):
        prompt("Please enter a positive number")
        loan_amount = input()

    # prompt user to enter the interest rate and check if the input is valid.
    # In order to prevent user input with %, strip % after input
    prompt('What is the annual interest rate')
    interest_rate = input().strip('%')

    while invalid_interest(interest_rate):
        prompt("Please enter a non-negative rate")
        interest_rate = input().strip('%')


    # prompt user to enter the loan amount and check if the input is valid
    prompt('What is the loan duration in year')
    year = input()

    while invalid_number(year):
        prompt("Please enter a positive number")
        year = input()

    # convert input for calcuation
    monthly_interest_rate = (float(interest_rate) / 100) / 12
    month = float(year) * 12
    loan_amount = float(loan_amount)

    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate / 
            (1 - ( 1+ monthly_interest_rate ) ** (-month)))
    else:
        monthly_payment = loan_amount / month # if 0 interest rate

    prompt(f"Your monthly payment is: ${monthly_payment:.2f}")

    prompt("Performance another calculation? (y/n)")
    answer = input().lower()
    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Performance another calculation? (y/n)')
        answer = input().lower()

    if answer[0] == 'n':
        break