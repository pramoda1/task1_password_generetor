import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ""
    
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    if not characters:
        print("Please include at least one character type (letters, numbers, or symbols).")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    include_letters = input("Include letters (yes/no)? ").lower() == 'yes'
    include_numbers = input("Include numbers (yes/no)? ").lower() == 'yes'
    include_symbols = input("Include symbols (yes/no)? ").lower() == 'yes'

    password = generate_password(length, include_letters, include_numbers, include_symbols)
    
    if password:
        print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
