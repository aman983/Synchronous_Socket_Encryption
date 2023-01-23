#server to recive
import socket
from random import *
def encrypt(text,c):
    result = ""
    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char != ' '):
            if (char.isupper()):  
                result += chr((ord(char) + c-65) % 26 + 65)

            # Encrypt lowercase characters
            else:
                result += chr((ord(char) + c - 97) % 26 + 97)
        #Do not encrypt space character 
        elif(char == ' '):
            result += chr(ord(' '))
    return result

def decrypt(text,d):
    c = 26 - d
    result = encrypt(text,c)
    return result 

def genkey(num):
    key_list = []
    for i in range(num):
        keys = randrange(1,26)
        key_list.append(keys)
    return key_list

# generate 100 random keys 
key_list = []
key_list = genkey(100)
send_key = str(key_list)

print()
print(f"generated Keys: {key_list}")
print()

nk = 0 #new key index 
n = 1  # control flow
key = 4 # initial key 

#Server startup configuration
LOCALHOST = input("Enter the IP address of the server --> ")
PORT = int(input("Enter the port of the server --> "))
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print()
print("Server started")
print("Waiting for client request..")

while True:
    clientConnection,clientAddress = server.accept()
    if n == 1:
        clientConnection.send(bytes(send_key,'UTF-8'))
        data = clientConnection.recv(1024)
        data_decode = data.decode()
        decipher_data = decrypt(data_decode,key)
        n = 0
        print("Dispatched Keys for client keys")
        print()
        print("SECURE CONNECTION HAS BEEN SUCCESSFULLY ESTABLISHED WITH ClIENT")
        print()
    
   
    if n == 0:
        # Now take one key at a time and then decrypt the data
        
        data = clientConnection.recv(1024)
        data_decode = data.decode()
        key = key_list[nk]
        
        decipher_data = decrypt(data_decode,key)
        print()
        print("Encrypted data recived from client --> :" , data_decode)
        print("Decrypted Data --> :" , decipher_data)
        nk += 1
        print("key value === ",key)
        print()
    clientConnection.close()
