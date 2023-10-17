from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #to fetch from front debug
from router.obra import obra

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
  obra,
  prefix="/obra",
  tags=["obra"]
)