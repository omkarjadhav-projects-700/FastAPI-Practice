from fastapi import FastAPI
import math

app = FastAPI()


@app.get("/")
async def welcome_message():
    return {"message": "Welcome!"}


@app.get("/factorial/{num}")
async def get_factorial(num: int):
    return {
        "number": num,
        "Factorial": math.factorial(num)
    }


@app.get("/e to power/{num}")
async def get_e_to_power(num: int):
    return {
        "number": num,
        "e to power {num}": math.exp(num)
    }
