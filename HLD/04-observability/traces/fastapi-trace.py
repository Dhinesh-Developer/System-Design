from fastapi import FastAPI, Request
import uuid
import time

app = FastAPI()

@app.middleware("http")
async def tracing_middleware(request: Request, call_next):
    trace_id = str(uuid.uuid4())
    start = time.time()

    print(f"TRACE START "
          f"trace_id={trace_id} "
          f"path={request.url.path}")
    
    response = await call_next(request)
    duration = time.time() - start

    print(
        f"TRACE END "
        f"trace_id={trace_id} "
        f"duration={duration:.3f}s"
    )

    response.headers["X-Trace-ID"] = trace_id
    return response

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    time.sleep(0.2)
    return {
        "order_id": order_id
    }


