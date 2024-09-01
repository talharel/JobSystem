from sqlalchemy.future import select
from models.companies import Company
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


class CompanyService:

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_companies(self):
        try:
            result = await self.db.execute(select(Company))
            company_list = result.scalars().all()
            return company_list

        except Exception as e:
            print('Error in companies service')
            print(e)
            raise HTTPException(status_code=500, detail='Backend Error')

    async def add_company(self, company_name: str, url: str) -> Company:
        try:
            new_company = Company(company_name=company_name, url=url)
            self.db.add(new_company)
            await self.db.commit()
            return new_company

        except Exception as e:
            print('Error in companies service')
            print(e)
            raise HTTPException(status_code=500, detail='Backend Error')
