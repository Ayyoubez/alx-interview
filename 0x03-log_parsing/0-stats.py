#!/usr/bin/python3

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    # Define the log entry format
    ip_format = "{:d}.{:d}.{:d}.{:d}"
    status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    # Create the log entry
    log_entry = (
        f"{ip_format.format(random.randint(1, 255), random.randint(1, 255), "
        f"{random.randint(1, 255)}, {random.randint(1, 255)}) - "
        f"[{datetime.datetime.now()}] \"GET /projects/260 HTTP/1.1\" "
        f"{random.choice(status_codes)} {random.randint(1, 1024)}\n"
    )
    # Write the log entry to stdout
    sys.stdout.write(log_entry)
    sys.stdout.flush()
