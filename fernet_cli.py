from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    return key

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message

def main():
    while True:
        print("1. Encrypt Message\n2. Decrypt Message\n3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            message = input("Enter message to encrypt: ").encode()
            key = generate_key()
            encrypted_message = encrypt_message(message, key)
            print("Encrypted Message: ", str(encrypted_message)[2:-1] , "\n")
            print("Key: ", str(key)[2:-1], "\n")
        elif choice == 2:
            encrypted_message = input("Enter message to decrypt: ").encode()
            key = input("Enter key: ").encode()
            decrypted_message = decrypt_message(encrypted_message, key)
            print("Decrypted Message: ", str(decrypted_message)[2:-1])
        elif choice == 3:
            exit()
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()