# Exponentia Backoff
# Implemetn an exponential backoff stratergy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1 # in seconds
max_tries = 5
attempts = 0

while attempts < max_tries:
    print(f"Attempt {attempts + 1}\nWait Time: {wait_time} seconds")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1