from pydantic import BaseModel


class Contact(BaseModel):
    contact_id:int
    first_name:str
    surname:str
    username:str
    password:str

    class Config:
        schema_extra = {
            "example": {
                "contact_id": 1,
                "first_name": "Jhon",
                "last_name": "Doe",
                "user_name": "jhon_123",
                "password": "*****"
            }
        }


class ContactOut(BaseModel):
    contact_id: int
    first_name: str
    surname: str
    username: str


