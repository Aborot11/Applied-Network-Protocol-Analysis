# IT6 Brute-force Challenge (Take Home Drill)

This project is my solution for the IT6 Take Home Drill.  
The goal was to systematically guess the 3-digit PIN (000-999) protecting a web application by crafting raw HTTP POST requests using sockets.

---

## Approach

- Scanned active ports with `netstat` and Wireshark to find that the app was running on `127.0.0.1:8888`

- Inspected the web form to see that it sends a POST to `/verify` with the field `magicNumber`

- Built a raw POST request manually in Python using the socket library.

- Brute-forced all PINs from 000 to 999 while respecting server pacing (at least 2 seconds per try)

- Detected success when the server **did not return "Incorrect number"** in the response.

---

## How to Run

1. Make sure `ctf1_for_x64.exe` server is running.
2. Then run:

cmd
python bruteforce.py
