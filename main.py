from fastapi import FastAPI
from app.routes.students import router as students_router

app = FastAPI(title="Student collection API")

app.include_router(students_router)
