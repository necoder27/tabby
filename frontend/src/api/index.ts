import axios from "axios"

const apiClient = axios.create({
  baseURL: 'http://tabby.dashboard:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
