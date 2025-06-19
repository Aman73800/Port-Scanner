import socket
import threading

print_lock = threading.Lock()

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            with print_lock:
                print(f"[+] Port {port} is OPEN")
        sock.close()
    except socket.error:
        pass

def main():
    target = input("Enter target IP or domain: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    print(f"\n🔍 Scanning {target} from port {start_port} to {end_port}...\n")

    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        thread.start()

if __name__ == "__main__":
    main()
