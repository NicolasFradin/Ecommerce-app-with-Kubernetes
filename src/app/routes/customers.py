from fastapi import APIRouter
router = APIRouter(
    prefix="/customers",
    tags=["customers"],
    #dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)
@router.get("/", tags=["customers"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/me", tags=["customers"])
async def read_user_me():
    return {"username": "fakecurrentuser"}

@router.get("/{username}", tags=["customers"])
async def read_user(username: str):
    return {"username": username}