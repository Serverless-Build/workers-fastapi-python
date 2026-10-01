from fastapi import FastAPI
from pydantic import BaseModel, Field
from workers import asgi

MARKER = "SERVERLESS_BUILD_FASTAPI_PYTHON_V1"
app = FastAPI(title="Workers FastAPI quote calculator", version="1.0.0")


class QuoteRequest(BaseModel):
    quantity: int = Field(ge=1, le=100, description="Number of items")
    unit_price_cents: int = Field(ge=1, le=100000, description="Price in integer cents")


@app.get("/")
async def index():
    return {"pattern": "FastAPI on Python Workers", "marker": MARKER,
            "endpoints": ["GET /health", "POST /quote", "GET /openapi.json", "GET /docs"]}


@app.get("/health")
async def health():
    return {"ok": True, "marker": MARKER}


@app.post("/quote")
async def quote(body: QuoteRequest):
    return {"quantity": body.quantity, "total_cents": body.quantity * body.unit_price_cents,
            "marker": MARKER}


# Workers supplies the ASGI server; there is no uvicorn process or socket listener.
Default = asgi.entrypoint(app)
