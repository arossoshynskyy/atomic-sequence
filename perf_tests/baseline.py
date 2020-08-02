import threading


class LockingSequence:
    def __init__(self, value):
        self.value = value
        self.lock = threading.Lock()

    def get(self):
        with self.lock:
            return self.value

    def set(self, value):
        with self.lock:
            self.value = value

    def increment_and_get(self, value):
        with self.lock:
            self.value += value
            return self.value

    def get_and_increment(self, value):
        with self.lock:
            old_value = self.value
            self.value += value
            return old_value
