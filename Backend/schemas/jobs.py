from pydantic import BaseModel, field_validator


class JobDetails:
    def __init__(self, company_name, job_url, platform_name):
        self.company_name = company_name
        self.job_url = job_url
        self.platform_name = platform_name

    def __str__(self):
        return f"JobDetails(company_name='{self.company_name}', job_url='{self.job_url}')"


class Job_StatusRequest(BaseModel):
    job_id: int
    status: str

    @field_validator('status')
    def validate_status(cls, status: str):
        statuses = ['viewed', 'not_viewed', 'star']
        if status not in statuses:
            raise ValueError('status is not valid.')
        return status
