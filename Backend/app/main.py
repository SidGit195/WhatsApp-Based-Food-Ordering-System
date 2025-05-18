from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
import app.models            # register models

from app.settings import settings
from app.routers import menu, orders
from app.routers.whatsapp import router as wa_router

# create tables
Base.metadata.create_all(bind=engine)

# init app
app = FastAPI(title="WhatsApp Food Ordering")

# CORS — allow your React dev server (or use ["*"] for everything)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount routers
app.include_router(menu.router)
app.include_router(orders.router)
app.include_router(wa_router)

@app.get("/")
async def root():
    return {"message": "Welcome to WhatsApp Food Ordering API"}