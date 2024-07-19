import os

import uvicorn
from fastapi import FastAPI
from routes import routes

host: str = os.environ.get("HOST", "0.0.0.0")
port: int = int(os.environ.get("PORT", "8082"))

app: FastAPI = FastAPI(
    title="Smart Report Generator",
    version="0.0.1",
)
app.include_router(routes)

print("http://localhost:" + str(port) +"/docs")
if __name__ == '__main__':
    uvicorn.run("app:app", host=host, port=port, reload=True)

