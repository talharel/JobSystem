from database import Base
from sqlalchemy import Column, Integer, String


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, index=True)
    url = Column(String)
    platform_name = Column(String)
    status = Column(String, index=True)
