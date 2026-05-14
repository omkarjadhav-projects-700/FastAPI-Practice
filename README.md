# Production Grade FastAPI

## Project Overview

This repository contains a small FastAPI-based web service designed to demonstrate modern Python API development best practices, configuration management, request validation, and Docker containerization.

The app exposes a simple math API with robust input validation and structured JSON responses, making it a suitable portfolio project for backend development and API design.

## Key Features

- FastAPI framework for high performance and developer productivity
- Clean application structure under `app/`
- Pydantic models for request and response validation
- Environment-aware configuration using `pydantic-settings`
- Docker support for reproducible deployment
- Detailed logs and JSON-formatted logging setup

## Repository Structure

- `dockerfile` - Docker image definition for building and running the app
- `requirements.txt` - Python package dependencies
- `app/main.py` - FastAPI application entrypoint, route definitions, and middleware
- `app/config.py` - Application settings and environment configuration
- `app/schemas.py` - Pydantic schemas used for validation and serialization
- `tests/test_math.py` - Unit tests for core math functionality

## Technologies Used

- Python 3.11
- FastAPI
- Uvicorn
- Pydantic / pydantic-settings
- Docker
- pytest

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd fastapi
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install application dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application locally:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

5. Open the API documentation in your browser:

   ```
   http://localhost:8000/docs
   ```

## Docker Usage

Build the Docker image:

```bash
docker build -t fastapi-new .
```

Run the container:

```bash
docker run -d -p 8000:8000 fastapi-new
```

Verify the service is running:

```bash
docker ps
```

## API Endpoints

### GET `/`

Returns a health check or landing response for the API.

### POST `/calculate`

Accepts a JSON body with a numeric value and returns the result of a math operation.

Example request payload:

```json
{
  "number": 5.0,
  "operation": "square"
}
```

Example response payload:

```json
{
  "number": 5.0,
  "result": 25.0,
  "operation": "square"
}
```

> Note: The exact endpoint details may vary slightly depending on implementation. Use the interactive docs at `/docs` for the current contract.

## Testing

Run the unit tests with pytest:

```bash
pytest
```

## Project Highlights

- Designed to show API design capability and clean Python development practices
- Uses FastAPI request validation and response models to ensure correctness
- Supports Docker for easy environment consistency and deployment
- Includes structured settings management for production-ready configuration

## Future Improvements

- Add more math operations and calculation endpoints
- Implement authentication and rate limiting
- Add comprehensive API versioning and more integration tests
- Add CI/CD pipeline configuration

## Contact

For questions or code review, please reach out during the interview or use the repository notes for follow-up details.
