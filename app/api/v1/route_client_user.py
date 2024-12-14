from fastapi import APIRouter
from sqlalchemy.orm import sessionmaker
# from .config.settings import settings 



router = APIRouter(
    # prefix="/"",
    responses={404: {"description": "Not found"}},
    
)

@router.post("/client_user")
def post_client_user(
    user = 

   
    return ()


