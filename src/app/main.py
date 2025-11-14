from fastapi import FastAPI
from app.testing.dto import Applicant
from app.testing.logic import is_eligible_for_loan

app = FastAPI(
    title="Rag Project",
    description="Latest Project"
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/loan-eligibility")
def is_eligible_loan(applicant: Applicant) -> dict:
    eligiblity_status = is_eligible_for_loan(applicant.income, applicant.age, applicant.employee_status)
    return {'eligibility_status': eligiblity_status}
