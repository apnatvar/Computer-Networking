import socket
import os
import time
import getpass
import hashlib

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096
password = "3b213ced003e89b35a26c22cbd011c9bfab29578415b2069f7fc8b01998b903d"

def recieveData():
    host = "127.0.1.2"
    port = 5001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(10)
    print(f"[*] Listening as {host}:{port}")
    print("Waiting for the client to connect... ")
    client_socket, address = s.accept()
    print(f"[+] {address} is connected.")
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = os.path.basename(filename)
    filesize = int(filesize)
    with open(filename, "wb") as f:
        while True:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            f.write(bytes_read)
    client_socket.close()
    s.close()
    time.sleep(1)
    print(f"File {filename} received successfully from {address[0]}")
    print("Connection Aborted")

def sendData():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = str(input("Enter the IP Address to connect to: "))
    port = int(input("\nEnter the port number to connect to: "))
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected to ", host)
    filename = str(input("Enter the full address of the file you need to transfer: "))
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    print(f"File {filename} successfully sent to {host}")
    print("Connection Aborted")
    s.close()

def recieveOrSendData():
    print("Enter the option number to send new data to a server or request update on blockchain")
    print("Option 1: Send New Data")
    print("Option 2: Recieve Updated Blockchain")
    print("Option 3: Exit the Program")
    inputFromUser = str(input("Enter here: "))
    if (inputFromUser == "1"):
        sendData()
    elif (inputFromUser == "2"):
        recieveData()
    elif (inputFromUser == "3"):
        exit()
    else :
        print("Invalid Option.")
    recieveOrSendData()

def authenticate():
    print("\n\n\n\n***************************************************************************************************************")
    print("Before proceeding please verify the Username and Password")
    usernameInput = getpass.getuser()
    print(f"Welcome: {usernameInput}")
    passwordInput = getpass.getpass("Password:")
    print("Authenticating...")
    testing = (passwordInput).encode()
    passwordInput = str(hashlib.sha256(testing).hexdigest())
    if (password == passwordInput):
        print("Password correct.")
        recieveOrSendData()
    else:
        print("Authentication failed. Program will now exit.")
    print("***************************************************************************************************************\n\n\n")

authenticate()
