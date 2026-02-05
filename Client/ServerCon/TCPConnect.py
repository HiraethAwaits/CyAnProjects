import socket
import threading

# Proxy Server Configuration
proxy_host = '127.0.0.1'
proxy_port = 8888

# Destination Server Configuration
destination_host = 'google.com'
destination_port = 80

def handle_client(client_socket): 
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((destination_host, destination_port))

    while True:
        client_data = client_socket.recv(4096)
        if len(client_data) == 0:
            break

        server_socket.send(client_data)
    
    client_socket.close()
    server_socket.close()

def start_proxy():
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy.bind((proxy_host, proxy_port))

    proxy.listen(5)
    print(f"Proxy server listening on {proxy_host}: {proxy_port}")

    while True:
        client_socket, addr = proxy.accept()
        print(f"Accepted connection from {addr[0]}: {addr[1]}")

        client_handle = threading.Thread(target=handle_client, args=(client_socket,))
        client_handle.start()

if __name__ == "__main__":
    start_proxy()