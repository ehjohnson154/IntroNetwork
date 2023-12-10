import threading
import time

from chatui import init_windows, read_command, print_message, end_windows
#from chatuicurses import init_windows, read_command, print_message, end_windows

def runner():
    count = 0

    while True:
        time.sleep(2)
        print_message(f"*** Runner count: {count}")
        count += 1

init_windows()

t1 = threading.Thread(target=runner, daemon=True)
t1.start()

while True:
    try:
        command = read_command("Enter a thing> ")
    except:
        break

    print_message(f">>> {command}")

end_windows()
