from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import airbnb_router
import os

FRONTEND_DOMAIN_NAME = os.getenv("FRONTEND_DOMAIN_NAME", None)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000",
    "https://airbnb-finder.up.railway.app/",
    "https://airbnb-finder.up.railway.app",
    "https://airbnb-finder.up.railway.app:3000",
]

#if FRONTEND_DOMAIN_NAME is not None:
#    origins.append(f'https://{FRONTEND_DOMAIN_NAME}')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(airbnb_router.router, prefix="/api")
