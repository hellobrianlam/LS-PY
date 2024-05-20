# Calculator

## Description
This is a simple calculator program that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. The program supports both English and Spanish languages for user prompts.

## Assignment
This project is an assignment from Launch School Course PY101, Lesson 2.

## Features
- Supports addition, subtraction, multiplication, and division operations.
- Provides user prompts in English and Spanish.
- Validates user input for numbers and operators.
- Allows users to perform multiple calculations in a single session.

## Requirements
- Python 3.10

## Installation
1. Clone the repository or download the source code.

```bash
git clone https://github.com/hellobrianlam/LS-PY.git
cd backend/PY101/lesson_2/calculator/
```

2. Ensure you have Python 3.10 installed on your system. You can download it from python.org.

3. Make sure you have the prompt.json file in the same directory as the Python script. The prompt.json file should contain the following content:

```json
{
    "en": { 
        "welcome": "Welcome to Calculator!", 
        "invalid_prompt": "Hmm... that doesn't look like a valid number.",
        "first_number": "What's the first number?", 
        "second_number": "What's the second number?",
        "operator": "What operation would you like to perform? \n1[+]) Add 2[-]) Subtract 3[*]) Multiply 4[/]) Divide",
        "invalid_operator": "You must choose 1[+], 2[-], 3[*], or 4[/]",
        "result": "The result is {output}",
        "restart": "Perform another calculation? (y/n)",
        "zero_error": "Cannot divide by zero.",
        "bye": "Goodbye!",
        "change_lang": "Select a language (en/es):",
        "lang_error": "Invalid choice. Please choose 'en' for English or 'es' for Spanish.",
        "change_rounding": "Enter new rounding value:",
        "invalid_number": "Invalid number. Please enter a valid number.",
        "config": "Configuration Options:\n1) Change language\n2) Change rounding value\n3) Continue",
        "yes": ["y", "yes"],
        "invalid_option": "Invalid choice. Please select 1, 2, or 3."
    }, 
    "es": { 
        "welcome": "¡Bienvenido a la calculadora!", 
        "invalid_prompt": "Hmm... eso no parece un número válido.",
        "first_number": "¿Cuál es el primer número?", 
        "second_number": "¿Cuál es el segundo número?",
        "operator": "¿Qué operación te gustaría realizar? \n1[+]) Sumar 2[-]) Restar 3[*]) Multiplicar 4[/]) Dividir",
        "invalid_operator": "Debes elegir 1[+], 2[-], 3[*], o 4[/]",
        "result": "El resultado es {output}",
        "restart": "¿Realizar otro cálculo? (s/n)",
        "zero_error": "No se puede dividir por cero.",
        "bye": "¡Adiós!",
        "change_lang": "Seleccione un idioma (en/es):",
        "lang_error": "Elección inválida. Por favor elige 'en' para inglés o 'es' para español.",
        "change_rounding": "Ingrese un nuevo valor de redondeo:",
        "invalid_number": "Número inválido. Por favor ingrese un número válido.",
        "config": "Opciones de configuración:\n1) Cambiar idioma\n2) Cambiar valor de redondeo\n3) Continuar",
        "yes": ["s", "sí", "si"],
        "invalid_option": "Elección inválida. Por favor seleccione 1, 2 o 3."
    }
}
```

## Usage
1. Run the calculator.py script.
```bash
python calculator.py
```
2. The program will display a welcome message in English and prompt you to choose a language ('en' for English, 'es' for Spanish).

3. Follow the prompts to enter the first number, the second number, and the operation you would like to perform.

4. The program will display the result and ask if you want to perform another calculation.

5. Enter 'y' to perform another calculation or 'n' to exit the program.


```plaintext
==> Welcome to Calculator!
Choose language ('en' for English, 'es' for Spanish): es
==> ¡Bienvenido a la calculadora!
---------------------------------
==> ¿Cuál es el primer número?
10
==> ¿Cuál es el segundo número?
20
==> ¿Qué operación te gustaría realizar? 
1) Sumar 2) Restar 3) Multiplicar 4) Dividir
1
==> El resultado es 30.0
==> ¿Realizar otro cálculo? (y/n)
n
```
