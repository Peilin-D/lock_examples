import threading
import time

def printer(idx):
    while True:
        print("Hello from Thread {}".format(idx))

if __name__ == '__main__':
    for threadidx in range(4):
        th = threading.Thread(target=printer,
                              args=(threadidx,))
        th.daemon = True  # exit even when this thread is alive
        th.start()
    time.sleep(5)
