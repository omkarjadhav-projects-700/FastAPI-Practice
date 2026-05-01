from fastapi import FastAPI
from math import exp

app = FastAPI()



@app.get("/")
def welcome():
    return {"Welcome!!"}


@app.post("/etox")
def expo(number: float):
    return {"number": number, "e_to_the_number": exp(number)}