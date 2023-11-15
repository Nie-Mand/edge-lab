import time
from threading import Thread


class Ticker:
    def __init__(self, every=1, callback=None):
        self.every = every
        self.callback = callback

    def start(self):
        thread = Thread(target=self._start)
        thread.start()

    def _start(self):
        while True:
            time.sleep(self.every)
            if self.callback:
                self.callback()
