from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI(title="SmartBin API")

app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/bins")
def bins():
    return [{"id":1,"name":"Bin A","fill_level":70}]
