from fastapi import FastAPI, Request, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import shutil
from web import interface

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Render html files
templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/getstate")
def state():
    return {"state":"light is off"}

@app.post("/submitaudio")
async def user(audio_data: UploadFile = File(...)):
    with open('audio.wav', 'wb') as f:
        shutil.copyfileobj(audio_data.file, f)
    print("Done")
    command = _activate('audio.wav', "Hausa")
    print(command)
    return command

def _activate(audio_data, lang):
    command = interface(audio_data, lang)
    return command


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.0', port=8000)