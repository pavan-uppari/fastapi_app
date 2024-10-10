from fastapi import APIRouter
from core.entity import User
from database import user_table

user = APIRouter()


@user.get("/users")
def get_users() -> list[User]:

    users = user_table.find()
    return [User(**user) for user in users]

@user.post("/users/")
def create_user(user: User) -> User:

    user_table.insert_one(user.model_dump())

    return user



