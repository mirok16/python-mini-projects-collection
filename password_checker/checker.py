def is_long_enough(password):
    return len(password) >= 8
def has_digit(password):
    return any(char.isdigit() for char in password)
