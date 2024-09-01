from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from services.companies import CompanyService
from schemas.companies import Company,CompanyRequest
from celery_tasks.companies import celery_task_find_word_in_companies

router = APIRouter(
    prefix='/companies',
    tags=['companies']
)


def get_company_service(db: AsyncSession = Depends(get_db)) -> CompanyService:
    return CompanyService(db)




@router.get('/')
async def get_companies(company_service: CompanyService = Depends(get_company_service)):
    companies_list = await company_service.get_companies()
    count = len(companies_list)
    return {'companies': companies_list,'count':count}




# from celery_tasks.companies import check_term_in_page

# @router.get('/search/{word}')
# async def search_word_in_companies(word,db=Depends(get_db)):
#     companyService = CompanyService(db)
#     all_companies = await companyService.get_companies()
#     companies = [company.company_name for company in all_companies if check_term_in_page(url=company.url, word='wwww')]
#     return {'companies': companies}




@router.get('/search/{word}')
async def search_word_in_companies(word: str,company_service=Depends(get_company_service)):
    companies = await company_service.get_companies()
    companies_json = [Company.model_validate(company).model_dump() for company in companies]
    task = celery_task_find_word_in_companies.delay(companies_json,word=word)
    companies_list = task.get()
    return {'companies': companies_list}


@router.post('/')
async def add_company(request: CompanyRequest, company_service=Depends(get_company_service)):
    company = await company_service.add_company(request.company_name, request.url)
    return {'company': company}
