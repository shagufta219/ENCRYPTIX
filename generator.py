import random
import string

def generate_password(length):
    # Define the character sets to use for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine the character sets
    all_chars = lowercase + uppercase + digits + special_chars

    # Generate the password
    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired password length: "))

    # Generate and display the password
    password = generate_password(length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()