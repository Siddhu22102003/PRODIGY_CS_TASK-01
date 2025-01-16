def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypt the message using Caesar Cipher."""
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII base for uppercase and lowercase
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabet characters remain the same
    
    return encrypted_text

def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypt the message using Caesar Cipher."""
    return caesar_encrypt(text, -shift)  # Decrypting is just reversing the shift

def main():
    print("\n=== Caesar Cipher Program ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    while True:
        choice = input("\nChoose an option (1, 2, or 3): ").strip()
        
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue
        
        message = input("Enter the message: ").strip()
        shift = int(input("Enter the shift value (integer): ").strip())
        
        if choice == '1':
            encrypted_message = caesar_encrypt(message, shift)
            print(f"\nEncrypted Message: {encrypted_message}")
        elif choice == '2':
            decrypted_message = caesar_decrypt(message, shift)
            print(f"\nDecrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
