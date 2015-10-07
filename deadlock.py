import threading
import time

def worker(A, B, lockA, lockB):
    while True:
        for idx in range(len(A)):
            with lockA:
                a = A[idx]
                if a > 0:
                    with lockB:
                        b = B[idx]
                        B[idx] = b + 1
                        A[idx] = a - 1

if __name__ == '__main__':
    A = range(10)
    B = range(10)
    lockA = threading.Lock()
    lockB = threading.Lock()

    for threadidx in range(8):
        if threadidx % 2 == 0:
            args = (A, B, lockA, lockB)
        else:
            args = (B, A, lockB, lockA)

        th = threading.Thread(target=worker, args=args)
        th.daemon = True  # exit even when this thread is alive
        th.start()

    for step in range(10):
        print(sum(A), sum(B))
        time.sleep(1)
