import threading
import time


def print_time(thread_name, delay):
    while True:
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        time.sleep(delay)


class Thread(threading.Thread):
    def __init__(self, thread_id, name, run, **run_k_args):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        self.name = name
        self._run = run
        self.run_k_args = run_k_args

    def run(self):
        if self.run_k_args is None:
            self._run(self.name)
        else:
            self._run(self.name, **self.run_k_args)


if __name__ == '__main__':
    # Create new threads

    thread1 = Thread(1, "Thread-1", print_time, delay=10)
    thread2 = Thread(2, "Thread-2", print_time, delay=5)

    # Start new Threads
    thread1.start()
    thread2.start()
