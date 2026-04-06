
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Employee Management API")

class Employee(BaseModel):
    name:str
    role:str
    salary:int

db=[]

@app.post("/employee")
def add_employee(emp:Employee):
    db.append(emp)
    return {"status":"added","employee":emp}

@app.get("/employees")
def get_employees():
    return db
