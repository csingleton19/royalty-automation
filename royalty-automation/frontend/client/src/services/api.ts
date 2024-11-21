// src/services/api.ts
import axios from 'axios';

const API_BASE_URL = 'http://localhost:5000'; // adjust as needed, make better later

export const api = {
  // PDF Extraction
  extractPdf: async (file: File) => {
    const formData = new FormData();
    formData.append('pdf', file);
    return axios.post(`${API_BASE_URL}/api/extraction/extract-pdf`, formData);
  },

  // Query Processing
  processQuery: async (query: string) => {
    return axios.post(`${API_BASE_URL}/query`, { query });
  },

  // Database Operations
  initializeDatabase: async () => {
    return axios.post(`${API_BASE_URL}/database/initialize`);
  },
  loadData: async () => {
    return axios.post(`${API_BASE_URL}/database/load`);
  },

  // Vector Database Operations
  uploadEmbeddings: async () => {
    return axios.post(`${API_BASE_URL}/embeddings/upload`);
  }
}