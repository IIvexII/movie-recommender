from fastapi import FastAPI
from deta import Deta

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
