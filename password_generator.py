import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Password length should be at least 4")

    # Build the character pool
    char_pool = ''
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        raise ValueError("No character types selected!")

    # Ensure at least one character from each selected category
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices
    while len(password) < length:
        password.append(random.choice(char_pool))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

# Example usage:
print("Generated password:", generate_password(length=16))
