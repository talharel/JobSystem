import axios from 'axios';
import {backendUrl} from '../utils/constants'

const apiClient = axios.create({
  baseURL: backendUrl,
});

export default apiClient;
