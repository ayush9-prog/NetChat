import socket

# 1. Define the Server's IP and Port to connect to
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 65432

# 2. Create the client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Connect to the server
try:
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print(f"[+] Successfully connected to the server at {SERVER_HOST}:{SERVER_PORT}")
    print("Type your message and press Enter. Type 'exit' to quit.\n")
    
    # 4. Communication loop
    while True:
        user_message = input("[You]: ")
        client_socket.send(user_message.encode('utf-8'))
        
        if user_message.lower() == 'exit':
            print("[-] Disconnecting...")
            break
            
        # Wait for the server's custom reply
        server_reply = client_socket.recv(1024).decode('utf-8')
        
        if not server_reply or server_reply.lower() == 'exit':
            print("[-] Server ended the chat session.")
            break
            
        print(f"[Server]: {server_reply}")

except ConnectionRefusedError:
    print("[-] Could not connect to the server. Is server.py running?")

finally:
    # 5. Close the socket
    client_socket.close()
    print("[*] Client closed.")