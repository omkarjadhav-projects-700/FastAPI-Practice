from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import math
import time
import logging
from app.config import settings
from contextlib import asynccontextmanager


### Logging:
logging.basicConfig(
    format= '{"time": "%(asctime)s",' \
    '"level": "%(levelname)s",' \
    '"msg": "%(message)s"}',

    level = logging.INFO
)

logger = logging.getLogger(__name__)



@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up Math API")
    yield
    logger.info("Shutting down")



app = FastAPI(
    title=settings.app_name,
    version=settings.version,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)


### CORS (Cross Origin Resource Sharing)
### Cors is a browser security mechanism that controls which websites can make requests to the API.

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_methods=["GET"],
    allow_headers=["*"], ### Any website can call the API
)


### Request latency logging middleware:

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    latency = (time.perf_counter() - start) * 1000
    logger.info(f"{request.method} {request.url.path} → {response.status_code} ({latency:.1f}ms)")
    response.headers["X-Response-Time-Ms"] = str(round(latency, 1))
    return response


### Global Exception Handling:

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error on {request.url.path}: {exc}")
    return JSONResponse(status_code=500, content={"error": "Internal server error"})


### Health ckeck for docker and kubernetes:

@app.get("/health", tags=["infra"])
async def health():
    return {"status": "ok", "version": settings.version}


###----------------------------ROUTES---------------------

### HOMEPAGE:
@app.get("/", tags = ["general"])
async def welcome_message():
    return {"message": "Welcoem to Math API",
            "version": settings.version}



@app.get("/factorial/{num}", tags = ["Math"])
async def get_factorial(num: int):
    if num<0:
        raise HTTPException(status_code = 400, detail="Enter the number greater than or equal to zero.")
    if num>70:
        raise HTTPException(status_code=400, detail="Number is too large. Enter the number between 0 and 70")
    
    return {
        "number": num,
        "Factorial": math.factorial(num)
    }


@app.get("/e^num/{num}")
async def get_e_to_power(num: float):
    if num > 100:
        raise HTTPException(status_code=400, detail="Entered number is too large. Enter the number less than or equal to 100")
    return {
        "number": num,
        "e^ {num}": math.exp(num)
    }


@app.get("/favicon.ico")
async def favicon():
    return FileResponse("favicon.ico")

