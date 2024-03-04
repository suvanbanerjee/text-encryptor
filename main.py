import aes_cipher
from pyscript import document

def encrypt(a):
    print(a)
    input_text = document.querySelector("#plain_text")
    input_text = input_text.value
    key = document.querySelector("#pass")
    key = key.value
    data_encrypter = aes_cipher.DataEncrypter()
    data_encrypter.Encrypt(input_text.encode(), key)
    encrypted_message = data_encrypter.GetEncryptedData()
    output_div = document.querySelector("#output")
    output_div.innerText = "Encrypted Message: " + str(encrypted_message)[2:-1] + "\n" + "Key: " + str(key)[2:-1] + "\n"
