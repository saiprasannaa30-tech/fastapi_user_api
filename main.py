from fastapi import FastAPI
from routers.users import router as user_router
from middleware.headers import add_custom_header

app = FastAPI(title="User API")

app.middleware("http")(add_custom_header)

app.include_router(user_router)

@app.get("/")
def home():
    return {"message": "FastAPI is running"}
