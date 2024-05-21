# Calculator

## Description
This is a simple calculator program developed as an assignment for Launch School Course PY101, Lesson 2. The calculator supports basic arithmetic operations and allows the user to select the language for prompts.

## Features
- Supports addition, subtraction, multiplication, and division operations.
- Allows user to choose between English and Spanish for prompts.
- Handles invalid input.
- Allows user to change rounding precision.
- Checks for division by zero and handles it appropriately.

## Requirements
- Python 3.6+

## Installation
1. Clone the repository or download the source code.

```sh
git clone https://github.com/hellobrianlam/LS-PY.git
cd backend/PY101/lesson_2/calculator/
```

2. Ensure you have Python installed on your system (Python 3.6+ recommended).


## Usage
1. Run the calculator.py script.
```sh
python calculator.py
```
2. Follow the prompts to perform calculations.

## Running the Program
1. When you start the program, you will see a welcome message.
2. You will be prompted to configure options like language and rounding precision.
3. Enter the numbers and choose the operation you want to perform.
4. The result will be displayed, and you will be asked if you want to perform another calculation. 

```sh
==> Welcome to Calculator!
==> Configuration Options:
1) Change language
2) Change rounding value
3) Continue
==> 3
---------------------------------
==> What's the first number?
5
==> What's the second number?
10
==> What operation would you like to perform? 
1) Add [+] 2) Subtract [-] 3) Multiply [*] 4) Divide [/]
==> 1
==> The result is 15.0
==> Perform another calculation? (y/n)
n
==> Goodbye!

```


## Code Overview
The main components of the program are:
- Global Variables: ROUND_VALUE and LANGUAGE are defined at the module level.
- Prompt Functions: Functions like prompt, get_message are used to display messages.
- Validation Functions: Functions to validate input, such as is_invalid_number and get_valid_number.
- Configuration Functions: Functions to change language and rounding precision.
- Calculation Functions: Functions to perform arithmetic operations and handle zero division.