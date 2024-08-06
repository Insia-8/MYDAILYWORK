import random

def generate_password(length):
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:",.<>?/`~'
    
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation
    
    password = ''
    for i in range(length):
        password += random.choice(all_characters)

    return password


print("Length must be a positive integer.")
length = int(input("Enter the desired length for the password: "))


password = generate_password(length)
print("Generated Password:", password)

