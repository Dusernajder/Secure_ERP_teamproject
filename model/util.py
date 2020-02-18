import random
import string


def get_combination(items, n):
    return [random.choice(items) for _ in range(n)]


def generate_id(number_of_small_letters = 4,
                number_of_capital_letters = 2,
                number_of_digits = 2,
                number_of_special_chars = 2,
                allowed_special_chars = r"_+-!"):

    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = [char for char in allowed_special_chars]

    arr = get_combination(lowercase_letters, number_of_small_letters)
    arr += get_combination(uppercase_letters, number_of_capital_letters)
    arr += get_combination(digits, number_of_digits)
    arr += get_combination(special_characters, number_of_special_chars)
    random.shuffle(arr)
    return ''.join(arr)
