// components/VectorDBManager.tsx
import React, { useState } from 'react';
import { api } from '../services/api';

export const VectorDBManager: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleUploadEmbeddings = async () => {
    setLoading(true);
    try {
      await api.uploadEmbeddings();
      alert('Embeddings uploaded successfully');
    } catch (err) {
      setError('Failed to upload embeddings');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Vector Database Management</h2>
      <button onClick={handleUploadEmbeddings} disabled={loading}>
        Upload Embeddings
      </button>
      {error && <div className="error">{error}</div>}
    </div>
  );
};