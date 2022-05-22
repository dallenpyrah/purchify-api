from fastapi import Depends, FastAPI
from Routers import AuthorizationRouter

app = FastAPI()
app.include_router(AuthorizationRouter.router)