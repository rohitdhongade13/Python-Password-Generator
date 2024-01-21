import secrets
import string

def generate_password(length=12):
    # Define character sets for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one of each type of character
    password = (secrets.choice(string.ascii_uppercase) +
                secrets.choice(string.ascii_lowercase) +
                secrets.choice(string.digits) +
                secrets.choice(string.punctuation))

    # Generate the remaining characters for the password
    password += ''.join(secrets.choice(characters) for _ in range(length - len(password)))

    # Shuffle the characters to make the password more secure
    password_list = list(password)
    secrets.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print(f"Generated Password: {generated_password}")
