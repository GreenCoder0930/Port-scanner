import asyncio

ascii_art = r"""
  ____            _   ____                  
 |  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
 | |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
 |  __/ (_) | |  | |_ ___) | (_| (_| | | | |
 |_|   \___/|_|   \__|____/ \___\__,_|_| |_|
                                            
"""
print(ascii_art)
print("For educational and ethical use only.\n")

def valid_ip(ip):
    import ipaddress
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

async def scan_port(target, port):
    try:
        conn = asyncio.open_connection(target, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        print(f"[+] Port {port} is open")
        writer.close()
        await writer.wait_closed()
    except Exception:
        pass  # Ignore errors, port is closed

async def main():
    target = input("Target IP or hostname: ")
    if not valid_ip(target):
        print("Invalid IP address!")
        return

    try:
        start_port = int(input("Start port: "))
        end_port = int(input("End port: "))
        if not (0 < start_port <= 65535 and 0 < end_port <= 65535):
            print("Ports must be between 1 and 65535.")
            return
        if start_port > end_port:
            print("Start port must be less than or equal to end port.")
            return
    except ValueError:
        print("Please enter valid port numbers.")
        return

    print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
    tasks = [scan_port(target, port) for port in range(start_port, end_port + 1)]
    await asyncio.gather(*tasks)
    print("\nScan complete.")

if __name__ == "__main__":
    asyncio.run(main())

print("\nScan complete.")
input("Press Enter to close the program...")
