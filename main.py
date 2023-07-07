from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from constants.origins import origins
from routes.index import appRouter

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
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
