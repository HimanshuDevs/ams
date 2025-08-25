from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .views import handle_create_user, handle_login, handle_get_user, handle_create_department, handle_get_department
from config.database import get_async_db
from .schemas import UserLoginSchema, CreateUserForm, CreateDepartmentSchema
from utils.jwt_token import get_current_user

router = APIRouter()

@router.post('/create-user')
async def create_user(request: CreateUserForm, db: AsyncSession = Depends(get_async_db)):
    return await handle_create_user(request,db)

@router.post('/login')
async def login(request: UserLoginSchema, db:AsyncSession=Depends(get_async_db)):
    return await handle_login(request,db)

@router.get('/get-users-list')
async def get_users_list(db: AsyncSession = Depends(get_async_db), current_user: dict = Depends(get_current_user)):
    return await handle_get_user(db, current_user)

@router.post('/create-department')
async def create_department(request: CreateDepartmentSchema, db: AsyncSession = Depends(get_async_db), current_user: dict = Depends(get_current_user)):
    return await handle_create_department(request, db,current_user)

@router.get('/get-departments-list')
async def get_departments_list(db: AsyncSession = Depends(get_async_db), current_user: dict = Depends(get_current_user)):
    return await handle_get_department(db, current_user)