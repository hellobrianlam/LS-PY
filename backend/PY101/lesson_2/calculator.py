def prompt(message):
    '''
    prepend the marker to the front of each output string we pass to print
    '''
    print(f"==> {message}")

def invalid_number(number_str):
    '''
    1. the int() function tried to conv the given string to integer.
    2. if conv is successful, the input is a valid num. return False as
        it is False of invalid number
    3. use try/except statement to catch the ValueError and return True 
        of invalid number
    '''
    try:
        int(number_str)
    except ValueError:
        return True

    return False

prompt('Welcome to Calculator!')

prompt("What's the first number?")
number1 = input()

while invalid_number(number1):
    '''
    1. checks whether the input is valid
    2. the loop ends if the input is valid
    3. if invalid tells the user that the input is invalid use prompt
    4. waits for the next input as number1 = input()
    5. repeated
    '''
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()

prompt("What's the second number?")
number2 = input()

while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

prompt("""What operation would you like to perform?
    1) Add 2) Subtract 3) Multiply 4) Divide")""")
operation = input()

while operation not in ["1", "2", "3", "4"]:
    '''
    similar as the invalid_number function.
    the loop ends if the input is in ["1", "2", "3", "4"]
    if invalid then prompt user
    waits for the next input for operation = input()
    '''
    prompt("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    # Each comparison compares the variable operation with a different value.
    # This kind of logic is the use-case that the match case statement was
    # designed to handle
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is {output}")