#!/usr/bin/python3
import sys
import signal

# Initialize counters and data structures
total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """Prints the statistics gathered so far."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

def signal_handler(sig, frame):
    """Handle the keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 7:
            continue
        ip, _, _, date, method, url, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7], parts[8]
        
        if method != "\"GET" or url != "/projects/260" or protocol != "HTTP/1.1\"":
            continue
        
        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)