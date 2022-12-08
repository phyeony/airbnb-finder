from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import airbnb_router
import os

FRONTEND_DOMAIN_NAME = os.getenv("FRONTEND_DOMAIN_NAME", "localhost")
FRONTEND_PORT = os.getenv("FRONTEND_PORT","3000")

app = FastAPI()

origins = [
    f"http://{FRONTEND_DOMAIN_NAME}:{FRONTEND_PORT}",
    f"{FRONTEND_DOMAIN_NAME}:{FRONTEND_PORT}"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(airbnb_router.router, prefix="/api")