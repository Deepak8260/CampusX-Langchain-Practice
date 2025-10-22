from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str
    age: int = Field(default=18, description="Age of the student, default is 18") # default value is set using Fied
    location: str = 'India' # default value is set directly
    language:Optional[str] = None
    email:EmailStr
    cgpa:float = Field(gt=0 , le=10,default=None , description='A decimal value representing CGPA of a student')


new_student = {"name":"Deepak" , "email":"abc@gmail.in" , 'cgpa':10}
# new_student = {"name":"Deepak" , 'language':'English'}
student = Student(**new_student)
print(student)

student_dict = dict(student)
print(student_dict['name'])

student_json = student.model_dump_json()
print(student_json)


# new_stud = {"name":"Deepak","age":'32'} # even if age must be int, but we have given 32 and it worked bcoz due to coercing
# stud = Student(**new_stud)
# print(stud)