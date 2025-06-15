import axios from 'axios';

const API = axios.create({
  baseURL: process.env.REACT_APP_API_BASE,
});

export const login = (credentials) => API.post('/login', credentials);

export const predict = (features, token) =>
  API.post('/predict', { features }, {
    headers: { Authorization: token }
  });
