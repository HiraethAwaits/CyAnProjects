import time
import re
from collections import defaultdict

LOG_FILE = "auth.log"
FAIL_REGEX = re.compile(r"failed password for .* from (\d+\.\d+\.\d+\.\d+)")
THRESHOLD = 5
TIME_WINDOW = 60

failed_attempts = defaultdict(list)

def alert(ip):
    print(f"[!] ALERT: Multiple failed login attempts from {ip}!")

def simulate_log_read():
    with open(LOG_FILE, "r") as f:
        for line in f:
            yield line
            time.sleep(0.5)

def check_line(line, currect_line):
    match = FAIL_REGEX.search(line)
    if match:
        ip = match.group(1)
        failed_attempts[ip].append(current_time)

        failed_attempts[ip] = [t for t in failed_attempts[ip] if current_time - t < TIME_WINDOW]

        if len(failed_attempts[ip]) >= THRESHOLD:
            alert(ip)
            failed_attempts[ip].clear()

def main():
    print(f"[*] Simulated IDS monitoring {LOG_FILE} ... \n")
    for line in simulate_log_read():
        now = time.time()
        check_line(line, now)

if __name__ == "__main__":
    main()