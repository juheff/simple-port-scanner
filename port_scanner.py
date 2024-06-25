#!/usr/bin/env python3

import socket
import argparse
from datetime import datetime

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    
    # Translate host to IP address
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print(f"Hostname {host} could not be resolved.")
        return
    
    print(f"IP Address: {ip}")

    # Scan ports
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

    print("Scan completed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("host", type=str, help="Host to scan")
    parser.add_argument("--start-port", type=int, default=1, help="Starting port")
    parser.add_argument("--end-port", type=int, default=1024, help="Ending port")
    
    args = parser.parse_args()
    start_time = datetime.now()
    scan_ports(args.host, args.start_port, args.end_port)
    end_time = datetime.now()
    print(f"Scanning finished in: {end_time - start_time}")
