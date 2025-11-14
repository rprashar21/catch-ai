def is_eligible_for_loan(income:float,age:int,employment_status:float)->bool:
    return (income>=50000) and (age>=21) and (employment_status=='employed')
