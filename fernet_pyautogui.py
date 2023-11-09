from cryptography.fernet import Fernet
import pyautogui

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
        choice = pyautogui.confirm(text='Choose an option', title='Fernet Encryption', buttons=['Encrypt Message', 'Decrypt Message', 'Exit'])
        if choice == 'Fernet Encryption':
            message = pyautogui.prompt(text='Enter message to encrypt: ', title='Encrypt Message', default='')
            message = message.encode()
            key = generate_key()
            encrypted_message = encrypt_message(message, key)
            pyautogui.alert(text='Encrypted Message: ' + str(encrypted_message)[2:-1] + '\nKey: ' + str(key)[2:-1], title='Encrypted Message', button='OK')
        elif choice == 'Decrypt Message':
            encrypt_message = pyautogui.password(text='Enter message to decrypt: ', title='Decrypt Message', default='', mask='*')
            encrypted_message = encrypt_message.encode()
            key = pyautogui.password(text='Enter key: ', title='Decrypt Message', default='', mask='*')
            key = key.encode()
            decrypted_message = decrypt_message(encrypted_message, key)
            pyautogui.alert(text='Decrypted Message: ' + str(decrypted_message)[2:-1], title='Decrypted Message', button='OK')
        elif choice == 'Exit':
            exit()
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()