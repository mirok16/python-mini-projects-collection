def is_long_enough(password):
    return len(password) >= 8
def has_digit(password):
    return any(char.isdigit() for char in password)
def is_valid(password):
    return is_long_enough(password) and has_digit(password)
