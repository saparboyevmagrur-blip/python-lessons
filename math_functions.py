PI = 3.14
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def find_max(*numbers):
    if len(numbers) == 0:
        return None
    max_value = numbers[0]
    for number in numbers:
        if number > max_value:
            max_value = number

    return max_value