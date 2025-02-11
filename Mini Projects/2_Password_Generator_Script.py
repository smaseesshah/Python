# Password Generator Script
import random as r
import string as s

def password_generator(length):

    characters = list(s.ascii_letters + s.digits + s.punctuation)
    
    password_list = [r.choice(characters) for _ in range(length)]
    password = "".join(password_list)
    return password

def main():
    print("Welcome to the Random Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired password length (e.g., 12): "))
            if length < 1:
                print("Password length must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the password length.")
    
    generated_password = password_generator(length)
    print("\nYour generated password is:")
    print(generated_password)

if __name__ == '__main__':
    main()
