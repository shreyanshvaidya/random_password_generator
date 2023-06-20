import random


def generate_password(length):
    password = ''
    numbers = "0123456789"
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijlkmnopqrstuvwxyz"
    symbols = "!@#$%^&&*?><+-_"
    total_char = upper_letters + numbers + lower_letters + symbols

    for _ in range(length):
        random_index = random.randint(0, len(total_char) - 1)
        password += total_char[random_index]

    return password


# Example usage
password_length = int(input("enter the length of the password:"))
if password_length >= 0:
    generated_password = generate_password(password_length)
    print()
    print("the generated password: ",generated_password)
else :
    print("Invalid Input!")
