
from fastapi import FastAPI

app = FastAPI(title="SmartBin API")

@app.get("/")
def root():
    return {"message":"SmartBin API running"}

@app.get("/bins")
def bins():
    return [{"id":1,"name":"Bin A","fill_level":70}]
