import socket
import os
from blockchain import Blockchain
import time
import getpass
import threading
import hashlib

BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
password = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
ports = [ 5000, 5001, 5002 ] #server is limited to 3 connections at one time. This is a hardcoded limit for the purpose of demonstration of the project

def writeData(address, filename="sample.txt"):
    file = open(filename, "r")
    data = file.readlines()
    Blockchain.execute(data)
    file.close()
    os.remove(filename)
    print(f"Data successfully added to the blockchain by {address[0]}")

def recieveData(client_socket, address, s, port):
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
    writeData(address, filename)
    s.close()
    ports.append(port)
    print(f"File {filename} received successfully from {address[0]}")
    print(f"Connection to {address[0]} successfully aborted after transmission")

def sendData():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = str(input("Enter the IP Address to connect to: "))
    port = int(input("Enter the Port Number to connect to: "))
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host, port))
    print("[+] Connected to ", host)
    filename = "doc.json"
    filesize = os.path.getsize(filename)
    s.send(f"{filename}{SEPARATOR}{filesize}".encode())
    with open(filename, "rb") as f:
        while True:
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                break
            s.sendall(bytes_read)
    s.close()
    print(f"File {filename} succesfully sent to {host}")
    print("Connection Aborted")

def recieveOrSendData():
    print("Enter the option number to send new data to a server or request update on blockchain")
    print("Option 1: Send Updated Blockchain")
    print("Option 2: Receive data")
    print("Option 3: Exit the Program")
    inputFromUser = str(input("Enter here: "))
    if (inputFromUser == "1"):
        sendData()
    elif (inputFromUser == "2"):
        threadFunction()
    elif (inputFromUser == "3"):
        exit()
    else :
        print("Invalid Option.")
    recieveOrSendData()

def threadFunction():
    host = "127.0.2.2"
    set = False
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(15)
        if (ports == []):
            print("No more Ports are available for use\nFree previous connections to proceed further.")
            while ports==[]:
                pass
        if set:
            abort = str(input("To abort all new connections enter 1, to continue recieving press Enter\n"))
            if abort == "1":
                print("No new connections will be made. Waiting on previous connections to complete.")
                thread.join()
                recieveOrSendData()
        port = ports[0]
        s.bind((host, port))
        s.listen()
        print(f"[*] Listening as {host}:{port}")
        print("Waiting for the clients to connect... ")
        try:
            client_socket, address = s.accept()
            ports.remove(port)
            print(f"[+] {address} is connected.")
            set = True
            thread = threading.Thread(target=recieveData, args=(client_socket, address, s, port))
            thread.start()
        except TimeoutError:
            print("No Client tried to connect, closing all new connections")
            s.close()
            #thread.join()
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
