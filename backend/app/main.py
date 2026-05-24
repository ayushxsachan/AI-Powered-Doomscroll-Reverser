from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.routers import ai, analysis, health, share

settings = get_settings()

app = FastAPI(
    title="Doomscroll Reverser API",
    version="1.0.0",
    description="AI-powered productivity analysis API for Doomscroll Reverser.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_private_network_cors_header(request, call_next):
    response = await call_next(request)
    if request.headers.get("access-control-request-private-network") == "true":
        response.headers["Access-Control-Allow-Private-Network"] = "true"
    return response


app.include_router(health.router)
app.include_router(analysis.router)
app.include_router(ai.router)
app.include_router(share.router)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Doomscroll Reverser API is online."}
