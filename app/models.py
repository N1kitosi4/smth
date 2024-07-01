from pydantic import BaseModel


class UserOut(BaseModel):
    id: int
    email: str
    created: bool

    class Config:
        from_attributes = True
