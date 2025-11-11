import axios from 'axios';

export const http = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 30000,
  headers: {
    'Content-Type': 'application/json',
  },
});

http.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

http.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    const errorMessage = error.response?.data?.message || error.message || 'Невідома помилка';

    const customError = {
      message: errorMessage,
      status: error.response?.status,
      data: error.response?.data,
    };

    return Promise.reject(customError);
  }
);

export default http;
