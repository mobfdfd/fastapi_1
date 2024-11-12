from fastapi import FastAPI
from app.database.database import engine, Base
from app.routers import upload_router, analyze_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(upload_router.router)
app.include_router(analyze_router.router)
