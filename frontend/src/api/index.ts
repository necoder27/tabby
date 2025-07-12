import axios from "axios"

const apiClient = axios.create({
  baseURL: 'http://tabby.dashboard:8888',
  headers: {
    'Content-Type': 'application/json',
  },
});

export default apiClient;
