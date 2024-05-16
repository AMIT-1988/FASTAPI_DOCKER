from typing import Union
from App.api.v1.user import router
from fastapi import FastAPI

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}
app.include_router(router)