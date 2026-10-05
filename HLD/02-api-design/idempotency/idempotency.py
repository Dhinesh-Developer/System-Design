from fastapi import FastAPI, Header
app = FastAPI()

processed_requests = {}

@app.post("/payments")
def make_payment(amount: float, idempotency_key: str = Header(...)):
    # check whether this request was already processed
    if idempotency_key in processed_requests:
        return {
            "message": "Already processed",
            "result": processed_requests[idempotency_key]
        }

    #simulate payment
    payment_result = {
        "status":"success",
        "amount":amount
    }

    # Store result
    processed_requests[idempotency_key] = payment_result
    return payment_result

