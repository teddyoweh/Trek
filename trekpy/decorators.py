import time

def timemycode(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] took {end_time - start_time:.5f} seconds to execute.")
        return result
    return wrapper
