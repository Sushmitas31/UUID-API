# UUID-API

## Overview
This FastAPI application provides two endpoints:
- `/uuid`: Generates a version 4 UUID instantly.
- `/async-uuid`: Generates a version 4 UUID with a 3-second, non-blocking delay.

## Requirements
- Python 3.12 or higher
- Poetry for dependency management
- Docker for containerization

## Setup & Installation
1. Clone this repository
2. Install dependencies using Poetry
    ```bash
    poetry install
3. Run code
    ```bash
    poetry run uvicorn src.uuid_assignment.app:app --host 0.0.0.0 --port 8000;  

## Endpoints
1. GET /uuid
    - Returns an immediate UUID v4.
2. GET /async-uuid
    - Returns a UUID v4 after a 3-second non-blocking delay.

## Docker

1. Command to build docker image
    ```bash
    docker build -t uuid-assignment:latest .
    ```
2. Command to run docker image
    ```bash
    docker run -p 8000:8000 uuid-assignment:latest
    ```

