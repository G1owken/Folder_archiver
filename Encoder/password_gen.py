import secrets
import string
def generate_random_password(length=12):
    if length < 10:
        raise ValueError("Password length should be at least 10 characters.")
    categories = [
        string.ascii_uppercase,
        string.ascii_lowercase,  
        string.digits, 
        string.punctuation 
    ]
    password = [secrets.choice(category) for category in categories]
    all_characters = ''.join(categories)
    password += [secrets.choice(all_characters) for _ in range(length - 4)]
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

