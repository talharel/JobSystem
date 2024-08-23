class JobDetails:
    def __init__(self,company_name,job_url,platform_name):
        self.company_name = company_name
        self.job_url = job_url
        self.platform_name = platform_name

    def __str__(self):
        return f"JobDetails(company_name='{self.company_name}', job_url='{self.job_url}')"