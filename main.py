from routes.index import appRouter
from constants.origins import origins
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

PORT = os.environ("PORT") if os.environ("PORT") else 8000


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Confirm Server is Running


@app.get("/")
def read_root():
    return {"message": "App is up and running"}


app.include_router(appRouter)

if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=PORT, reload=True)
