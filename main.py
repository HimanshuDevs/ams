from fastapi import FastAPI, Depends
from apps.accounts.routes import router as accounts_router
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  # your login endpoint path here


app = FastAPI(
    title="Attendance Management System API",
    description="Enter your Bearer token in the Authorize button to access protected routes.",
    version="1.0.0"
)

@app.get("/protected-route/")
async def protected_route(token: str = Depends(oauth2_scheme)):
    return {"token_received": token}

app.include_router(accounts_router, prefix='/accounts',tags=['User'])