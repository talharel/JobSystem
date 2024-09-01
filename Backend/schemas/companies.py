from pydantic import BaseModel, field_validator


class Company(BaseModel):
    id: int
    company_name: str
    url: str

    class Config:
        from_attributes = True


class CompanyRequest(BaseModel):
    company_name: str
    url: str



