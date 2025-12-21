import time
import tracemalloc

class Performance:
    def __init__(self):
        self.expanded = 0
        self.explored = 0

    def __enter__(self):
        tracemalloc.start()
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.time() - self.start_time
        current, peak = tracemalloc.get_traced_memory()
        self.current_memory = current
        self.peak_memory = peak
        tracemalloc.stop()
