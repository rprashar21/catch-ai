from fastapi import FastAPI
from app.testing.dto import Applicant
from app.testing.logic import is_eligible_for_loan
import logging

app = FastAPI(
    title="Rag Project",
    description="Latest Project"
)

logging.basicConfig(
    level=logging.INFO,
    # how to show ur log in brackets line number abd thn
    #        timestamp    line number         logging level
    format="[%(asctime)s] (line %(lineno)d) - %(levelname)s) - %(message)s",
    datefmt="%m-%d-%Y %H:%M:%S"
)



@app.get("/")
def read_root():
    logging.info("hitting debug point :{}")
    return {"message": "Hello World"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/loan-eligibility")
def is_eligible_loan(applicant: Applicant) -> dict:
    logging.info("loan endpoint callled")
    eligiblity_status = is_eligible_for_loan(applicant.income, applicant.age, applicant.employee_status)
    return {'eligibility_status': eligiblity_status}
