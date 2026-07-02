
from app.infrastructure.database.connection import db

from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str
    userid: str
    password: str
   

class MongoUserRepository():

    def __init__(self):
        self.collection = db["users"]

    async def find_one(self, userid: str) -> bool:

        document =  self.collection.find_one(
            {"userid": userid}
        )

        if document is None:
            return False

        return True

    async def insert_one(self, user: User) -> User:
        

        self.collection.insert_one(
            {
                "name": user.name,
                "userid": user.userid,
                "password": user.password
            }
        )

        return user

    async def get_by_id(self, userid: str) -> User | None:

        document = self.collection.find_one(
            {"userid": userid}
        )

        if document is None:
            return None

        return {
            "name" : document["name"],
            "userid" : document["userid"],
            "password" : document["password"]
        }