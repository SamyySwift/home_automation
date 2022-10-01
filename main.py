from fastapi import FastAPI
import uvicorn


app = FastAPI()
names = []
@app.get("/")
def home():
    return {"Text":"Hey samuel"}

@app.get("/api/getstate")
def state():
    return {"state":"light is off"}

@app.post("/api/username/{user_name}")
def user(user_name: str):
    names.append(user_name)
    
    return names


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)