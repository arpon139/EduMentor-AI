import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
db = client[os.getenv("DB_NAME", "edumentor")]


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    client.close()


app = FastAPI(title="EduMentor AI", lifespan=lifespan)

# React (Vite) ফ্রন্টএন্ডকে backend-এর সাথে কথা বলতে দেওয়ার জন্য
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "EduMentor AI backend চলছে"}


@app.get("/db-check")
async def db_check():
    # MongoDB-তে ping পাঠিয়ে কানেকশন ঠিক আছে কিনা দেখে
    await client.admin.command("ping")
    return {"database": "connected"}