import json

# Load messages from JSON file
with open('prompt.json', 'r') as file:
    MESSAGES = json.load(file)

def get_message(message_key, lang, **kwargs):
    return MESSAGES[lang][message_key].format(**kwargs)

def prompt(key, lang, **kwargs):
    '''
    Prepend the marker to the front of each output string we pass to print
    '''
    message = get_message(key, lang, **kwargs)
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
        user_input = input()
        if not is_invalid_number(user_input):
            return float(user_input)
        prompt('invalid_prompt', lang)

def get_valid_operator(lang):
    '''
    Repeatedly prompt the user for a valid operator input until a valid one is provided.
    '''
    valid_operators = {"1", "2", "3", "4"}
    while True:
        prompt('operator', lang)
        operation = input()
        if operation in valid_operators:
            return operation
        prompt('invalid_operator', lang)

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
        "1": number1 + number2,
        "2": number1 - number2,
        "3": number1 * number2,
        "4": number1 / number2
    }
    return round(operations[operation], 2)

def main():
    # Display the welcome message in the chosen language
    prompt('welcome', lang = 'en')

    # Prompt user for language selection
    lang = input("Choose language ('en' for English, 'es' for Spanish): ").strip().lower()
    while lang not in {'en', 'es'}:
        lang = input("Invalid choice. Please choose 'en' for English or 'es' for Spanish: ").strip().lower()


    
    while True:
        print("---------------------------------")
        number1, number2 = get_numbers(lang)
        operation = get_valid_operator(lang)
        result = calculate_result(number1, number2, operation)
        prompt('result', lang, output=result)

        prompt('restart', lang)
        answer = input().lower()
        while answer not in {'y', 'n'}:
            prompt('restart', lang)
            answer = input().lower()
        if answer == 'n':
            break

if __name__ == "__main__":
    main()
