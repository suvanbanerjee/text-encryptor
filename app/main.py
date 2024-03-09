import pycryp
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
    encrypted_message=pycryp.encrypt(input_text, key)
    output_div = document.querySelector("#output")
    output_div.innerText = "Encrypted Message\n\n" + str(encrypted_message)[2:-1]

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
        decrypted_message=pycryp.decrypt(input_text, key)
        output_div = document.querySelector("#output")
        output_div.innerText = "Decrypted Message\n\n" + str(decrypted_message)[2:-1]
    except:
        output_div = document.querySelector("#output")
        output_div.innerText = "Invalid Key or Encrypted Message"