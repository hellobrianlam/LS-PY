
import json

LANGUAGE = 'es'

# Open the JSON file for reading
with open('prompt.json', 'r') as file:
    MESSAGES = json.load(file)

def messages(message, lang):
    return MESSAGES[lang][message]

def prompt(key, output = None):
    '''
    prepend the marker to the front of each output string we pass to print
    '''
    message = messages(key, LANGUAGE).format(output=output)
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
        float(number_str) 
    except ValueError:
        return True

    return False

prompt('welcome')

while True:
    print("---------------------------------")
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        '''
        1. checks whether the input is valid
        2. the loop ends if the input is valid
        3. if invalid tells the user that the input is invalid use prompt
        4. waits for the next input as number1 = input()
        5. repeated
        '''
        prompt('invalid_prompt')
        number1 = input()

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_prompt')
        number2 = input()

    prompt('operator')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        '''
        similar as the invalid_number function.
        the loop ends if the input is in ["1", "2", "3", "4"]
        if invalid then prompt user
        waits for the next input for operation = input()
        '''
        prompt('invalid_operator')
        operation = input()

    match operation:
        # Each comparison compares the variable operation with a different value.
        # This kind of logic is the use-case that the match case statement was
        # designed to handle
        case "1":
            output = float(number1) + float(number2)
        case "2":
            output = float(number1) - float(number2)
        case "3":
            output = float(number1) * float(number2)
        case "4":
            output = float(number1) / float(number2)

    output = round(output, 2)  # Round the result to two decimals

    prompt('result', output)

    prompt('restart')
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('restart')
        answer = input().lower()

    if answer[0] != 'y':
        break
