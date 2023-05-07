from fastapi import FastAPI
import uvicorn
import os
from dotenv import load_dotenv
from routers import paraphrase_router


load_dotenv()
app = FastAPI()
app.include_router(paraphrase_router.router)


@app.get("/")
async def health_check():
    return {"status_code": 200,
            "detail": "ok",
            "result": "working"}

if __name__ == "__main__":
    uvicorn.run("main:app", host=os.getenv("HOST"), port=int(os.getenv("APP_PORT")), reload=True)