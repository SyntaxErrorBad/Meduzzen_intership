from fastapi import FastAPI
import uvicorn
from config import settings

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
    uvicorn.run("main:app", host=settings.host,port=settings.port,reload=settings.reload)
