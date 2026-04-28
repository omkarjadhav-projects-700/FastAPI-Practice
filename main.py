from fastapi import FastAPI
from math import exp

app = FastAPI()


@app.get("/")
def exponent():
    return {exp(5)}