import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6): "))
            if length < 6:
                print("Password length must be at least 6 characters. Try again.")
                continue
            password = generate_password(length)
            print(f"Your new generated password is: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
