import socket
from datetime import datetime

# Function to scan ports
def port_scanner(target, start_port, end_port):
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")

    # Loop through the specified port range
    for port in range(start_port, end_port + 1):
        # Set up a socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Try to connect to the port
        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is open")
        sock.close()

# Example usage
target_ip = input("Enter the IP address to scan: ")
start_port = 1
end_port = 1024
port_scanner(target_ip, start_port, end_port)
