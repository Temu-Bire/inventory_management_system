from pydantic import BaseModel

class SupplierCreate(BaseModel):
    name: str
    contact_info: str

class SupplierResponse(BaseModel):
    id: int
    name: str
    contact_info: str

    class Config:
        orm_mode = True