import time
import random
import math

class Scheduler:
    def __init__(self, l, nbr_messages, cb):
        self.cb = cb
        self.l = l
        self.nbr_messages = nbr_messages

    def run(self):
        _time = 0
        l = self.l
        nbr_messages = self.nbr_messages

        i = 0
        while i < nbr_messages:
            tt = self._next_time_interval(l)
            print("Publishing Time:", _time)
            time.sleep(tt)
            _time += tt
            self.cb()
            i = i + 1

    def _next_time_interval(self, l):
        n = random.random() * 1.0
        inter_event_time = - math.log(1.0 - n) / l
        return inter_event_time