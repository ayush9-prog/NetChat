import socket

# 1. Define the IP address and Port
# '127.0.0.1' is 'localhost' (your own computer)
HOST = '127.0.0.1'  
PORT = 65432        # Non-privileged ports are > 1023

# 2. Create a socket object
# AF_INET = IPv4, SOCK_STREAM = TCP (reliable connection)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Bind the socket to the host and port, then start listening
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"[*] Server is listening on {HOST}:{PORT}...")

# 4. Accept an incoming connection
client_socket, client_address = server_socket.accept()
print(f"[+] Connected to client at: {client_address}")

# 5. Interactive Communication loop
while True:
    try:
        # Wait and receive data from the client
        message = client_socket.recv(1024).decode('utf-8')
        
        if not message or message.lower() == 'exit':
            print("[-] Client disconnected.")
            break
            
        print(f"[Client]: {message}")
        
        # NEW: Server can now type a custom response!
        server_reply = input("[You (Server)]: ")
        client_socket.send(server_reply.encode('utf-8'))
        
        if server_reply.lower() == 'exit':
            print("[-] Shutting down connection...")
            break
        
    except ConnectionResetError:
        print("[-] Connection lost unexpectedly.")
        break

# 6. Clean up the connections
client_socket.close()
server_socket.close()
print("[*] Server shut down.")