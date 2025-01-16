# PRODIGY_CS_TASK-01

Secure AES Encryption Program
This is a simple Python program that implements AES encryption and decryption using the cryptography library. It allows users to securely encrypt and decrypt messages using a password and random salt for key derivation. The encryption process uses AES in CBC mode with a random initialization vector (IV), and the messages are padded to be AES-compatible using PKCS7 padding.

Features:
Key Generation: Derives a 256-bit encryption key from a user-provided password using the PBKDF2-HMAC key derivation function with SHA-256 hashing.
Encryption: Encrypts a message using AES (CBC mode) and outputs the encrypted message encoded in Base64.
Decryption: Decrypts the encrypted message back to its original plaintext.

Requirements:
Python 3.x
cryptography library (install via pip install cryptography)

How to Use:
Clone the repository to your local machine.
Run the program.
Set a password for encryption and decryption.
Choose whether to encrypt or decrypt a message.

Example usage:
python secure_encryption.py

![image](https://github.com/user-attachments/assets/927aa9cb-dd53-4af5-af81-a995b8cd4fdc)
