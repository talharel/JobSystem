from sqlalchemy import Column, Integer, String
from models.base_model import Base

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    url = Column(String)

