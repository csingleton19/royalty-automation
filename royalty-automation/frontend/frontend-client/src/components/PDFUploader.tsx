// frontend-client/src/components/PDFUploader.tsx
import React, { useState } from 'react';
import { api } from '../services/api';

export const PDFUploader: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);

  const handleUpload = async () => {
    if (file) {
      try {
        const response = await api.extraction.uploadPDF(file);
        console.log('Upload successful:', response.data);
      } catch (error) {
        console.error('Upload failed:', error);
      }
    }
  };

  return (
    <div>
      <input 
        type="file" 
        accept=".pdf"
        onChange={(e) => setFile(e.target.files?.[0] || null)} 
      />
      <button onClick={handleUpload}>Upload PDF</button>
    </div>
  );
};