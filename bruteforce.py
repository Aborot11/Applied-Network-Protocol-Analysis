# bruteforce.py
# IT6 Take Home Drill
# Goal: Brute-force a 3-digit PIN using raw sockets only

import socket

HOST = '127.0.0.1'
PORT = 8888  # Replace with actual port

# We'll try a basic POST request with a test PIN ("000")
test_pin = "000"
body = f"pin={test_pin}"

# Craft the raw HTTP request manually
request = (
    f"POST / HTTP/1.1\r\n"
    f"Host: {HOST}:{PORT}\r\n"
    f"Content-Type: application/x-www-form-urlencoded\r\n"
    f"Content-Length: {len(body)}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
    f"{body}"
)

# Try sending it
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request.encode())
        response = s.recv(4096).decode()
        print("[✓] Request sent")
        print("Response:")
        print(response)
except ConnectionRefusedError:
    print(f"[!] Failed to connect to {HOST}:{PORT}")
