from fastapi import FastAPI
from fastapi.responses import FileResponse
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


@app.get("/e^num/{num}")
async def get_e_to_power(num: int):
    return {
        "number": num,
        "e^ {num}": math.exp(num)
    }


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")
