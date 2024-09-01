import apiClient from '../utils/axios';

const jobService = {
  async getJobs() {
    try {
      const response = await apiClient.get('/jobs/', {});
      return response.data.jobs;
    } catch (error) {
      throw error;
    }
  },

  async getJobsDetails() {
    try {
      const response = await apiClient.get('/jobs/details', {});
      return response.data.details;
    } catch (error) {
      throw error;
    }
  },

  async searchJobs() {
    try {
      await apiClient.get('/jobs/update', {});
    } catch (error) {
      throw error;
    }
  },


  async updateStatus(job_id:number,status:string) {
    try {
      const response = await apiClient.patch('/jobs/status', {
        job_id,
        status
      });
      return response.data
      
    } catch (error) {
      throw error;
    }
  },

};

export default jobService;
