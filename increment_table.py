import threading
import time
import Queue

def worker(queue, table):
    while True:
        idx, value = queue.get()

        old_value = table[idx]
        time.sleep(0.01 + idx / 10000.0)  # simulate work
        table[idx] = old_value + value

        # update the amount of work left in the queue
        queue.task_done()

if __name__ == '__main__':
    queue = Queue.Queue()
    table = [0] * 5

    for threadidx in range(4):
        th = threading.Thread(target=worker,
                              args=(queue, table,))
        th.daemon = True  # exit even when this thread is alive
        th.start()

    start = time.time()
    for idx in range(100):
        queue.put((idx % len(table), 1))
    queue.join()  # wait for all messages to be processed
    end = time.time()

    print("Total {} in {} seconds".format(sum(table), end - start))
