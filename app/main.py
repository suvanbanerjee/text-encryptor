import aes_cipher
from pyscript import document
import base64

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
    data_encrypter = aes_cipher.DataEncrypter()
    data_encrypter.Encrypt(input_text, key)
    encrypted_message = data_encrypter.GetEncryptedData()
    output_div = document.querySelector("#output")
    # encrypted_message = bytes.hex(encrypted_message)
    encrypted_message = base64.b64encode(encrypted_message).decode('utf-8')
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
        data_encrypter = aes_cipher.DataDecrypter()
        input_text = base64.b64decode(input_text)
        data_encrypter.Decrypt(input_text, key)
        decrypted_message = data_encrypter.GetDecryptedData()
        output_div = document.querySelector("#output")
        output_div.innerText = "Decrypted Message\n\n" + str(decrypted_message)[2:-1]
    except:
        output_div = document.querySelector("#output")
        output_div.innerText = "Invalid Key or Encrypted Message"