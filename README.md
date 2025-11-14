# create a new project
uv init fastapi-projects
cd fastapi-projects

This automatically creates:
fastapi-project/
│── pyproject.toml     # like pom.xml
│── src/
│   └── fastapi_project/
│       └── __init__.py
│── .venv/             # uv-managed environment

uv add fastapi
uv add "uvicorn[standard]"

 Add FastAPI and Uvicorn using UV
uv add fastapi
uv add "uvicorn[standard]"




# create project structure 
mkdir -p src/app
mkdir -p tests


Add __init__.py files
Create these empty files to make the directories Python packages:
src/app/__init__.py
tests/__init__.py

# checking uv settings 
uv run which python

# change the python interpreter in the setting 
this u will need to do for every proejct 

# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run specific test file
uv run pytest tests/test_main.py


# run the server
uv run uvicorn app.main:app --reload

Open your browser: http://127.0.0.1:8000
API docs: http://127.0.0.1:8000/docs (Swagger UI)
Alternative docs: http://127.0.0.1:8000/redoc
Health check: http://127.0.0.1:8000/health