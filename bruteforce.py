# bruteforce.py



import socket  # We'll use the socket library for low-level HTTP communication

# Target server information (localhost and port from ctf1_for_x64.exe)
HOST = '127.0.0.1'
PORT = 8888  # Replace with actual port if different

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"[✓] Connected to {HOST}:{PORT}")
except ConnectionRefusedError:
    print(f"[!] Failed to connect to {HOST}:{PORT}")
