from fastapi import APIRouter, HTTPException, Query
from bson.objectid import ObjectId
from app.database import db
from app.schemas.student import StudentSchema, StudentResponseSchema
from typing import List, Optional

router = APIRouter(prefix="/students", tags=["Students"])

@router.post("/", response_model=dict, status_code=201)
async def create_student(student: StudentSchema):
    student_dict = student.dict()
    result = db.students.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@router.get("/", response_model=List[StudentResponseSchema])
async def list_students(
    country: Optional[str] = Query(None),
    age: Optional[int] = Query(None),
):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}

    students = list(db.students.find(query))
    return [
        {"id": str(student["_id"]), "name": student["name"], "age": student["age"], "address": student["address"]}
        for student in students
    ]

@router.get("/{id}", response_model=StudentResponseSchema)
async def fetch_student(id: str):
    student = db.students.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"id": str(student["_id"]), "name": student["name"], "age": student["age"], "address": student["address"]}

@router.patch("/{id}", status_code=204)
async def update_student(id: str, student: StudentSchema):
    update_data = {k: v for k, v in student.dict().items() if v is not None}
    result = db.students.update_one({"_id": ObjectId(id)}, {"$set": update_data})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    result = db.students.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
