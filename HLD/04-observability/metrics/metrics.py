import time
from fastapi import FastAPI
from prometheus_client import Counter,Histogram
from prometheus_client import generate_latest
from fastapi.responses import Response

app = FastAPI()

#count total HTTP requests
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)

#Measure request duration
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration"
)

@app.get("/products")
def get_products():
    start = time.now()
    REQUEST_COUNT.inc()
    time.sleep(0.2)
    duration = time.time() - start
    REQUEST_LATENCY.observe(duration)

    return{
        "products": ["Laptop","Phone"]
    }

@app.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )



