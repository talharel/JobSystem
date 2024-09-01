import apiClient from '../utils/axios';

const companyService = {
  async getCompanies() {
    try {
      const response = await apiClient.get('/companies/', {});
      return response.data;
    } catch (error) {
      throw error;
    }
  },

  async searchWordInCompany(word:string) {
    try {
      const response = await apiClient.get(`/companies/search/${word}`, {});
      return response.data.companies
    } catch (error) {
      throw error;
    }
  },

  async addCompany(company_name:string,url:string) {
    try {
      const response = await apiClient.post('/companies/', {company_name,url});
      return response
    } catch (error) {
      throw error;
    }
  },

}


export default companyService;