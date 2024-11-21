// src/components/PdfUploader.tsx
import React, { useState } from 'react';
import { api } from '../services/api';

export const PdfUploader: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;
    
    setLoading(true);
    try {
      const response = await api.extractPdf(file);
      console.log('Upload successful:', response.data);
    } catch (err) {
      setError('Failed to upload PDF');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <input type="file" accept=".pdf" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!file || loading}>
        {loading ? 'Uploading...' : 'Upload PDF'}
      </button>
      {error && <div className="error">{error}</div>}
    </div>
  );
};