import sys, time

def slow_text(text, min_delay = 0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(min_delay)

def slow_print(text, delay=1, new_line=True):
    slow_text(text)
    time.sleep(delay)
    print()
    if new_line:
        print()
