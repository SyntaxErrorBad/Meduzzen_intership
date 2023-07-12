from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],  # Дозволяє всі HTTP методи
    allow_headers=["*"],  # Дозволяє всі заголовки
)

@app.get("/")
def health_check():
    return {
        "status_code": 200,
        "detail": "ok",
        "result": "working"
    }

