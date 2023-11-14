from typing import Optional, Union
from pydantic import BaseModel, EmailStr, Field

from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, field):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(ObjectId(v))


class StudentSchema(BaseModel):
    # id: Union[str, None] = None
    id: Union[PyObjectId, None] = Field(default_factory=PyObjectId, alias="_id")
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }
        schema_extra = {
            "example": {
                "id": "123456789123456789123456",
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }

class UpdateStudentModel(BaseModel):
    id: Union[PyObjectId, None] = Field(default_factory=PyObjectId, alias="_id")
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            PyObjectId: str
        }
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}