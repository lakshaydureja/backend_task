import os
import uvicorn
from fastapi import FastAPI
from app.routes.students import router as students_router

app = FastAPI(title="Backend Intern Hiring Task")
app.include_router(students_router)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
