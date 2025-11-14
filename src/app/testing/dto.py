from pydantic import BaseModel, Field
from typing import Optional


class Applicant(BaseModel):
    income: float = Field(..., description="income should be provided")
    age: int
    employee_status: Optional[str] = " not working"


applicant = Applicant(income=22, age=21, employee_status='emp')  # this will work
applicant1 = Applicant(income=22, age=21)  # this will fail becoz inocem is required filed
print(applicant1)
