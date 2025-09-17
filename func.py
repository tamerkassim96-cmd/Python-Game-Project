import sys
import time

def slow_text(text, min_delay =0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(min_delay)
