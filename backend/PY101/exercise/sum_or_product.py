import math 
# from functools import reduce # for computer_product alternate method

def check_number(number_str):
    try:
        number = int(number_str)
        if number <= 0:
            raise ValueError
    except ValueError:
        return True

    return False

def check_operation(str):
    try:
        if str not in ['s', 'p']:
            raise ValueError
    except ValueError:
        return True
    return False


def get_number():
    prompt1 = "Please enter an integer greater than 0: "
    number = input(prompt1)

    while check_number(number):
        number = input(prompt1)

    return int(number)

def get_operation():
    prompt2 = 'Enter "s" to compute the sum, or "p" to compute the product: '
    operation = input(prompt2).lower()

    while check_operation(operation):
        operation = input(prompt2).lower()

    return operation

def compute_sum(target_num): 
    return sum(range(1, target_num+1))

# use math.prod
def compute_product(target_num):
    # alternate method
    # use functtools.reduce with lambda function
    # return reduce(lambda x, y: x * y, range(1, target_num + 1))
    return math.prod(range(1, target_num + 1))

def sum_or_product(number, operator):
  match operator:
    case 'p':
        print("The product of the integers between 1 and "
            f"{number} is {compute_product(number)}.")
    case 's':
        print("The sum of the integers between 1 and "
            f"{number} is {compute_sum(number)}.")

sum_or_product(get_number(), get_operation())
