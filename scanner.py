import socket

def scan_target(target_ip, port_range):
    print(f"Commencing scan on host: {target_ip}\n")
    
    for port in port_range:
        # Initialize a TCP socket (AF_INET = IPv4, SOCK_STREAM = TCP)
        scanner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a temporal constraint to prevent the script from stalling
        scanner_socket.settimeout(1.0)
        
        # Attempt the connection (metamorphosis from closed to established)
        result = scanner_socket.connect_ex((target_ip, port))
        
        if result == 0:
            print(f"[+] Port {port} is open.")
            
            # Initiate Banner Grabbing
            try:
                # Some services require a nudge to respond; sending a generic byte
                scanner_socket.send(b'Hello\r\n')
                banner = scanner_socket.recv(1024).decode().strip()
                if banner:
                    print(f"    [Service Identity]: {banner}")
            except Exception:
                print("    [Service Identity]: Unable to retrieve banner (quiescence).")
        
        scanner_socket.close()

if __name__ == "__main__":
    # Define the potency of our scan
    target = "127.0.0.1"  # Localhost for testing
    ports = range(20, 1025)  # Common service ports
    
    scan_target(target, ports)
