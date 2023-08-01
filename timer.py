import time
import random

class Timer:
    
    def __init__(self):
        self._time_ = None

    
    def timer_start(self):
        self._time_ = time.perf_counter_ns()

    
    def timer_stop(self):
        return time.perf_counter_ns() - self._time_



