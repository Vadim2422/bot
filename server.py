import uvicorn
from threading import Thread
from fastapi import FastAPI

app = FastAPI()


@app.head('/')
def home():
    return "Монитор"


def run():
    uvicorn.run('server:app', host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()
