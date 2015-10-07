import threading
import time

def printer(idx, lock):
    while True:
        with lock:
            print("Hello from Thread {}".format(idx))

if __name__ == '__main__':
    stdout_lock = threading.Lock()

    for threadidx in range(4):
        th = threading.Thread(target=printer,
                              args=(threadidx, stdout_lock))
        th.daemon = True  # exit even when this thread is alive
        th.start()
    time.sleep(5)
