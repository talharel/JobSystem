import apiClient from '../utils/axios';

const jobService = {
  async getTasks() {
    try {
      const response = await apiClient.get('/jobs/', {});
      return response.data.jobs;
    } catch (error) {
      throw error;
    }
  },
};

export default jobService;
