from pydantic import BaseModel, Field

class AddressSchema(BaseModel):
    city: str
    country: str

class StudentSchema(BaseModel):
    name: str
    age: int
    address: AddressSchema

class StudentResponseSchema(StudentSchema):
    id: str = Field(..., alias="_id")