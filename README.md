Asynchronous Port Scanner

An efficient asynchronous port scanner written in Python using `asyncio`.  
Developed for educational purposes and ethical hacking to analyze and test network security.

---

## Features

- Asynchronous scanning of TCP ports using `asyncio`
- Validates IP addresses and hostnames
- Scans a user-defined range of ports
- Displays open ports in real time
- Suitable for penetration testing (with authorization)

---

## Usage

Run with Python 3.7 or newer:

```bash
python3 port-scanner.py

You will be prompted to enter:

Target IP or hostname

Start port (1–65535)

End port (1–65535)


The scanner will check each port asynchronously and report any that are open.


---

Legal Notice

This tool is intended for educational use and authorized ethical hacking only.
Do not use it to scan systems you do not own or have explicit permission to test.
The author assumes no liability for misuse, damage, or illegal activity.


---

Requirements

Python 3.7 or higher

No external libraries required



---

License

MIT License — see the LICENSE file.
