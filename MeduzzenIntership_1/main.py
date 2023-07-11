from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import os

app = FastAPI()
#env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv("../venv/.env")

host = os.getenv("HOST")
port = int(os.getenv("PORT"))
reload = os.getenv("RELOAD")



@app.get("/")
def home():
    return {
        "status_code": 200,
        "detail" : "ok",
        "result" : "working"
        }

@app.get("/health")
def health():
    return {"status" : "Ok"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=host,port=port,reload=reload)
