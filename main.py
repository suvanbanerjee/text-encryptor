def password(key):  #Function to Generate key from Password
    key_fnl = ""
    for a in key:
        key_fnl = key_fnl + str(ord(a))
    return int(key_fnl)

def encrypt(msg,key):   #Function to Generate Encrypted Text
    enc_msg=[]
    for x in msg:
        char=int(ord(x))*int(key)
        char = str(char) + " "
        enc_msg.append(char)
    return enc_msg

def decrypt(enc_msg,fnl_key):   #Function to Decrypt Encrypted File
    fnl_msg=""
    for tmp in enc_msg:
        a=int(int(tmp)/int(fnl_key))
        fnl_msg = fnl_msg + chr(a)
    return fnl_msg
        
        
        
        
status=True


while status:
    
    
    #Printing Choice Menu
    print("Press 1 to Encrypt a message\nPress 2 to decrypt a messgae\nPress 3 to Exit\n\n")
    choice=input("Enter Choice ")
    
    
    
    if choice=="1":   #Encrypt Function Call
        msg=input("Enter Message\n ")
        key=input("Set a Password ")
        key_fnl = password(key)
        final_message = encrypt(msg,key_fnl)
        fil = open("out.enc",'w')
        fil.writelines(final_message)
        fil.close()
        
        
        
    elif choice=="2":   #Decrypt Function Call
        print("\n In the same directrory place the out.enc file\n")
        key=input("Password? ")
        fnl_key = password(key)
        fil = open("out.enc",'r')
        fila=fil.readline()
        fila=fila.strip(" ")
        fila = fila.split(" ")
        print("\nDecrypted Message is\n")
        print(decrypt(fila, fnl_key)+"\n\n")
        fil.close()
        
        
        
    elif choice=="3":   #Quit Program  
        status=False
        
        
           
    else:   #Invalid Input  
        print("\n\n\n\nInvalid Choice\n\n\n\n")
                
                
                
print("Thank You")
