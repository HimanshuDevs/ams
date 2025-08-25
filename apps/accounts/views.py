from fastapi import HTTPException, status
from .models import AuthUsers, DepartmentMaster
from utils.hashing import hash_password, verify_password
from utils.jwt_token import create_access_token
from sqlalchemy.future import select
from .schemas import GetUserSchema, GetDepartmentSchema

async def handle_create_user(request, db):
    user_data = AuthUsers(
        type         = request.type,
        full_name    = request.full_name,
        username     = request.username,
        email        = request.email,
        password     = hash_password(request.password)
    )
    print(hash_password(request.password))
    db.add(user_data)
    await db.commit()
    await db.refresh(user_data)

    return {
        "status": "success",
        "message": "User created successfully",
        "user": user_data
    }

async def handle_login(request, db):

    users_obj = select(AuthUsers).filter(AuthUsers.username == request.username)
    result = await db.execute(users_obj)
    user_obj = result.scalars().first()

    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid credentials 11122')
    
    if not verify_password(request.password, user_obj.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid password')
    user_data = {'user_id':user_obj.id, 'user_email':user_obj.email}
    access_token = create_access_token(user_data)
    return {"message":"Login successfully", "access_token":access_token}

async def handle_get_user(db,current_user):
    query = select(AuthUsers)
    result = await db.execute(query)
    users = result.scalars().all()
    return [GetUserSchema.from_orm(user) for user in users]

async def handle_create_department(request, db, current_user):
    new_dept = DepartmentMaster(
        department_name   = request.department_name,
        submitted_by      = current_user["user_id"]
    )
    db.add(new_dept)
    await db.commit()
    await db.refresh(new_dept)

    return {
        "status": "success",
        "message": "Created department successfully",
        "department": new_dept
    }

async def handle_get_department(db, current_user):
    query = select(DepartmentMaster)
    result = await db.execute(query)
    departments = result.scalars().all()
    return [GetDepartmentSchema.from_orm(department) for department in departments]