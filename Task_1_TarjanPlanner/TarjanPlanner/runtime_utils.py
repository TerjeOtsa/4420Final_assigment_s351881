import time


def log_runtime(func):
    """Decorator to log runtime of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        runtime = end_time - start_time
        print(f"\n[LOG] Function '{func.__name__}' executed in {runtime:.2f} seconds.\n")
        return result
    return wrapper