import aes_cipher
from pyscript import document

def encrypt(self):
    input_text = document.querySelector("#text")
    input_text = input_text.value
    key = document.querySelector("#pass")
    key = key.value
    if key == ""  and input_text == "":
        output_div = document.querySelector("#output")
        output_div.innerText = "Seriously? You want to encrypt nothing?"
        return
    if key == "" :
        output_div = document.querySelector("#output")
        output_div.innerText = "Set a Password"
        return
    if input_text == "":
        output_div = document.querySelector("#output")
        output_div.innerText = "Message can't be empty"
        return
    ScryptDefault = aes_cipher.Scrypt(16384, 8, 8)
    data_encrypter = aes_cipher.DataEncrypter(ScryptDefault)
    data_encrypter.Encrypt(input_text, key)
    encrypted_message = data_encrypter.GetEncryptedData()
    output_div = document.querySelector("#output")
    encrypted_message = bytes.hex(encrypted_message)
    output_div.innerText = "Encrypted Message\n\n" + str(encrypted_message)

def decrypt(self):
    input_text = document.querySelector("#text")
    input_text = input_text.value
    key = document.querySelector("#pass")
    key = key.value
    if key == ""  and input_text == "":
        output_div = document.querySelector("#output")
        output_div.innerText = "Seriously? You want to decrypt nothing?"
        return
    if key == "":
        output_div = document.querySelector("#output")
        output_div.innerText = "Provide a Password"
        return
    if input_text == "":
        output_div = document.querySelector("#output")
        output_div.innerText = "Message can't be empty"
        return
    try:
        ScryptDefault = aes_cipher.Scrypt(16384, 8, 8)
        data_encrypter = aes_cipher.DataDecrypter(ScryptDefault)
        data_encrypter.Decrypt(bytes.fromhex(input_text), key)
        decrypted_message = data_encrypter.GetDecryptedData()
        output_div = document.querySelector("#output")
        output_div.innerText = "Decrypted Message\n\n" + str(decrypted_message)[2:-1]
    except:
        output_div = document.querySelector("#output")
        output_div.innerText = "Invalid Key or Encrypted Message"