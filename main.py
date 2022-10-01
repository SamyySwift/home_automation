from fastapi import FastAPI
import uvicorn


app = FastAPI()

@app.get("/")
def home():
    return {"Text":"Hey samuel"}

@app.get("/api/getstate")
def state():
    return {"state":"light is off"}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)