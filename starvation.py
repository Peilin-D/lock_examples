import threading
import time

def worker(A, B, lock, sleeptime):
    while True:
        for idx in range(len(A)):
            with lock:
                time.sleep(sleeptime)
                a = A[idx]
                if a > 0:
                    b = B[idx]
                    B[idx] = b + 1
                    A[idx] = a - 1

if __name__ == '__main__':
    A = range(10)
    B = range(10)
    lock = threading.Lock()

    for threadidx in range(2):
        args = (A, B, lock, threadidx * 1)
        th = threading.Thread(target=worker, args=args)
        th.daemon = True  # exit even when this thread is alive
        th.start()

    for step in range(10):
        print(sum(A), sum(B))
        time.sleep(1)
