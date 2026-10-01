# FastAPI on Python Workers

A real ASGI API with Pydantic validation and generated OpenAPI documentation. The quote calculator uses integer cents to avoid floating-point currency errors; it does not create fake persisted orders.

## Pattern at a glance

| | |
|---|---|
| Difficulty | Beginner |
| Runtime | Python Workers |
| Framework | FastAPI |
| Data store | None |

## Setup and local development

Install Python 3.13+, uv, and Node.js 22+. Run `npm install && uv sync`, then `npm run dev`. Open `http://localhost:8787/docs` for the generated API explorer.

`workers.asgi.entrypoint(app)` connects FastAPI to the Workers runtime. Uvicorn is not needed.

## Test

```sh
curl http://localhost:8787/health
curl http://localhost:8787/quote -H 'content-type: application/json' \
  -d '{"quantity":3,"unit_price_cents":250}'
```

The total is 750 cents. Send a quantity of 0 or omit `unit_price_cents` to receive FastAPI's structured HTTP 422 validation errors. Inspect `/openapi.json` to see the same constraints in the schema.

## Deploy

Authenticate with `npx wrangler login`, run `npm run check`, then `npm run deploy`. Repeat the tests against the printed `workers.dev` URL. Only Python is offered here because FastAPI is a Python framework.

## Production fit

This is stateless validation and calculation. Add verified identity, request-size limits, and a persistence binding when your application needs stored records. Dependencies must support the Python Workers/Pyodide environment; the lock files make the tested package versions reproducible.

## References

- [FastAPI on Workers](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/)
- [Python Workers](https://developers.cloudflare.com/workers/languages/python/)

## Pattern and live demo

- [Pattern page](https://serverless.build/patterns/fastapi-workers)
- [Live deployment](https://workers-fastapi-python.dwarven.workers.dev)
