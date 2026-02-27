
from prometheus_client import generate_latest
from django.http import HttpResponse

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def metrics_view(request):
    """Expose Prometheus metrics, including log counters"""
    metrics = generate_latest()  # Generate all Prometheus metrics
    return HttpResponse(metrics, content_type='text/plain')