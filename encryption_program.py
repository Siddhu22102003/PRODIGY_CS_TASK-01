#Download Cryptography
#Command - " pip install cryptography "
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.padding import PKCS7
from cryptography.hazmat.backends import default_backend
import os
import base64

def generate_key(password: str, salt: bytes) -> bytes:
    """Generate a key from the given password and salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_message(message: str, key: bytes) -> str:
    """Encrypt the given message using AES encryption."""
    iv = os.urandom(16)  # Random Initialization Vector
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Pad the message to make it AES-compatible
    padder = PKCS7(128).padder()
    padded_message = padder.update(message.encode()) + padder.finalize()
    
    encrypted_message = encryptor.update(padded_message) + encryptor.finalize()
    return base64.b64encode(iv + encrypted_message).decode()

def decrypt_message(encrypted_message: str, key: bytes) -> str:
    """Decrypt the given message using AES decryption."""
    encrypted_data = base64.b64decode(encrypted_message)
    iv = encrypted_data[:16]  # Extract the Initialization Vector
    encrypted_content = encrypted_data[16:]
    
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_message = decryptor.update(encrypted_content) + decryptor.finalize()
    
    # Remove padding
    unpadder = PKCS7(128).unpadder()
    message = unpadder.update(padded_message) + unpadder.finalize()
    return message.decode()

def main():
    print("\n=== Secure Encryption Program (AES) ===")
    print("Features:")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    
    password = input("Set a password for encryption/decryption: ").strip()
    salt = os.urandom(16)  # Random salt for key derivation
    key = generate_key(password, salt)

    while True:
        choice = input("\nChoose an option (1, 2, or 3): ").strip()
        
        if choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        if choice not in ['1', '2']:
            print("Invalid choice. Please select 1, 2, or 3.")
            continue

        if choice == '1':
            message = input("Enter the message to encrypt: ").strip()
            encrypted = encrypt_message(message, key)
            print(f"\nEncrypted Message: {encrypted}")
        elif choice == '2':
            encrypted_message = input("Enter the encrypted message to decrypt: ").strip()
            try:
                decrypted = decrypt_message(encrypted_message, key)
                print(f"\nDecrypted Message: {decrypted}")
            except Exception as e:
                print(f"\nDecryption failed: {e}")

if __name__ == "__main__":
    main()
