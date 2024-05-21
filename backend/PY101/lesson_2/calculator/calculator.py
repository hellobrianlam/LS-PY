import json
import operator

# Load messages from JSON file
with open('prompt.json', 'r') as file:
    MESSAGES = json.load(file)

# Define global variables
ROUND_VALUE = 2
LANGUAGE = 'en'

def get_message(message_key, lang, output=None):
    message = MESSAGES[lang][message_key]
    if output is not None:
        message = message.format(output=output)
    return message

def prompt(key, lang, output=None):
    '''
    Prepend the marker to the front of each output string we pass to print
    '''
    message = get_message(key, lang, output)
    print(f"==> {message}")

def is_invalid_number(number_str):
    '''
    Checks if the provided string is a valid number.
    '''
    try:
        float(number_str)
        return False
    except ValueError:
        return True

def get_valid_number(prompt_key, lang):
    '''
    Repeatedly prompt the user for input until a valid number is provided.
    '''
    while True:
        prompt(prompt_key, lang)
        user_input = input().strip()
        if not is_invalid_number(user_input):
            return float(user_input)
        prompt('invalid_prompt', lang)

def get_valid_operator(lang):
    '''
    Repeatedly prompt the user for a valid operator input until a valid one 
    is provided.
    '''
    valid_operators = {
        "1": "add", "2": "sub", "3": "mul", "4": "truediv",
        "+": "add", "-": "sub", "*": "mul", "/": "truediv"
    }
    while True:
        prompt('operator', lang)
        operation = input().strip()
        if operation in valid_operators:
            return valid_operators[operation]
        prompt('invalid_operator', lang)

def check_zero_division(number2, operation, lang):
    '''
    Checks if the operation is division by zero.
    '''
    if zero_division(number2, operation):
        prompt('zero_error', lang)
        return True
    return False

def zero_division(number2, operation):
    '''
    Checks if the operation is division by 0.
    '''
    return number2 == 0 and operation == 'truediv'

def get_numbers(lang):
    '''
    Get the first number and the second number from the user.
    '''
    number1 = get_valid_number('first_number', lang)
    number2 = get_valid_number('second_number', lang)
    return number1, number2

def calculate_result(number1, number2, operation):
    '''
    Perform the calculation based on the chosen operator.
    '''
    operations = {
        "add": operator.add,
        "sub": operator.sub,
        "mul": operator.mul,
        "truediv": operator.truediv
    }
    result = operations[operation](number1, number2)
    return round(result, ROUND_VALUE)

def change_language():
    global LANGUAGE
    while True:
        prompt('change_lang', LANGUAGE)
        lang = input().strip().lower()
        if lang in {'en', 'es'}:
            LANGUAGE = lang
            break
        prompt('lang_error', LANGUAGE)

def change_rounding():
    global ROUND_VALUE
    while True:
        prompt('change_rounding', LANGUAGE)
        try:
            new_round = int(input().strip())
            if new_round > 0:
                ROUND_VALUE = new_round
                break
            raise ValueError
        except ValueError:
            prompt('invalid_number', LANGUAGE)

def config_options():
    while True:
        prompt('config', LANGUAGE)
        choice = input().strip().lower()
        if choice == '1':
            change_language()
        elif choice == '2':
            change_rounding()
        elif choice == '3':
            break
        else:
            prompt('invalid_option', LANGUAGE)

def restart(lang):
    '''
    Prompt the user to see if they want to perform another calculation.
    '''
    prompt('restart', lang)
    answer = input().strip().lower()
    return answer in MESSAGES[lang]['yes']

def calculate():
    print("---------------------------------")
    number1, number2 = get_numbers(LANGUAGE)
    operation = get_valid_operator(LANGUAGE)

    if check_zero_division(number2, operation, LANGUAGE):
        if not restart(LANGUAGE):
            return
        calculate()  # Restart the calculation

    result = calculate_result(number1, number2, operation)
    prompt('result', LANGUAGE, output=result)

    if restart(LANGUAGE):
        calculate()
    else:
        prompt('bye', LANGUAGE)

def main():
    prompt('welcome', LANGUAGE)
    config_options()
    calculate()

if __name__ == "__main__":
    main()
