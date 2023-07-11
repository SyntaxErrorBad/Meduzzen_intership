from fastapi import FastAPI
import uvicorn
from config import MySettings

app = FastAPI()

@app.get("/")
def home():
    return {
        "status_code": 200,
        "detail" : "ok",
        "result" : "working"
        }

@app.get("/health/{check}")
def health_check(check):
    return {
        "status_code": check,
        "detail": "ok",
        "result": "working"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host=MySettings().host,port=MySettings().port,reload=MySettings().reload)
