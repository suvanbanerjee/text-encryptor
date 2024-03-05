import aes_cipher
from pyscript import document

def encrypt(a):
    print(a)
    input_text = document.querySelector("#plain_text")
    input_text = input_text.value
    key = document.querySelector("#pass")
    key = key.value
    ScryptDefault = aes_cipher.Scrypt(16384, 8, 8)
    data_encrypter = aes_cipher.DataEncrypter(ScryptDefault)
    data_encrypter.Encrypt(input_text, key)
    encrypted_message = data_encrypter.GetEncryptedData()
    output_div = document.querySelector("#output")
    encrypted_message = bytes.hex(encrypted_message)
    output_div.innerText = "Encrypted Message: " + str(encrypted_message) + "\n" + "Key: " + str(key)
    print(encrypted_message)

def decrypt(a):
    input_text = document.querySelector("#decrypt_text")
    input_text = input_text.value
    key = document.querySelector("#decrypt_pass")
    key = key.value
    try:
        ScryptDefault = aes_cipher.Scrypt(16384, 8, 8)
        data_encrypter = aes_cipher.DataDecrypter(ScryptDefault)
        data_encrypter.Decrypt(bytes.fromhex(input_text), key)
        decrypted_message = data_encrypter.GetDecryptedData()
        output_div = document.querySelector("#output2")
        output_div.innerText = "Decrypted Message: " + str(decrypted_message)[2:-1]
    except:
        output_div = document.querySelector("#output2")
        output_div.innerText = "Invalid Key or Encrypted Message"
    print(decrypted_message)