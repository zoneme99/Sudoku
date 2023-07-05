import time

def calculate(function, *args, **kwargs):
    start_time = time.time()
    result = function(*args, **kwargs)
    end_time = time.time()
    the_return = end_time - start_time
    return the_return, result
