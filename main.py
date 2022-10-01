from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Text":"Hey samuel"}

@app.get("/api/getstate")
def state():
    return {"state":"light is off"}