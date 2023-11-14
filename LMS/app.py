from fastapi import FastAPI, status, HTTPException
from database import student_collection
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from models import StudentSchema, UpdateStudentModel, PyObjectId
from bson import ObjectId

app = FastAPI()

@app.post("/student/", response_description="Add new student", response_model=StudentSchema, status_code=status.HTTP_201_CREATED)
async def create_student(student: StudentSchema):
    student = jsonable_encoder(student)
    new_student = await student_collection.insert_one(student)
    created_student = await student_collection.find_one({"_id": new_student.inserted_id})
    return created_student

@app.get("/student/{id}", response_description="Get a single student", response_model=StudentSchema)
async def get_student(id: PyObjectId):
    if (student := await student_collection.find_one({"_id": id})) is not None:
        return student
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

@app.put("/student/{id}", response_description="Update a student", response_model=UpdateStudentModel)
async def update_student(id: PyObjectId, student: UpdateStudentModel):
    # id = ObjectId(id)
    student = {k: v for k, v in student.model_dump().items() if v is not None}
    if len(student) >= 1:
        update_result = await student_collection.update_one({"_id": id}, {"$set": student})
        if update_result.modified_count == 1:
            if (
                updated_student := await student_collection.find_one({"_id": id})
            ) is not None:
                return updated_student
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")

@app.delete("/student/{id}", response_description="Delete a student")
async def delete_student(id: PyObjectId):
    delete_result = await student_collection.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Student with ID {id} not found")