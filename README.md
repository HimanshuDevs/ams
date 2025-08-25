ATTENDANCE MANAGEMENT SYSTEM
fastapi
python version is Python 3.10.7

Steps to run the project 
1. setup the virtual enviornment
    python -m venv env
2. install the depedency
    pip install -r requirements.txt
3. run the project
    uvicorn main:app --reload
4. run the migration
    alembic upgrade head


Migrations
--> use alembic to manage the migrations
steps
1. pip install alembic 
2. alembic init alembic
3. alembic revision --autogenerate -m "create user" (to generate the migrations)
4. alembic upgrade head (to apply migrations in database)