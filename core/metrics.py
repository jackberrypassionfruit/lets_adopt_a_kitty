from prometheus_client import Counter
from functools import wraps

request_counter = Counter('num_requests_total', 'Total number of requests')

def inc_request_counter(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        
        request_counter.inc()
        
        return view_func(request, *args, **kwargs)
    return wrapper