// components/DatabaseManager.tsx
import React, { useState } from 'react';
import { api } from '../services/api';

export const DatabaseManager: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleInitialize = async () => {
    setLoading(true);
    setError(null); // Clear any previous errors
    try {
      await api.initializeDatabase();
      alert('Database initialized successfully');
    } catch (err) {
      setError('Failed to initialize database');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleLoadData = async () => {
    setLoading(true);
    setError(null); // Clear any previous errors
    try {
      await api.loadData();
      alert('Data loaded successfully');
    } catch (err) {
      setError('Failed to load data');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="database-manager">
      <h2>Database Management</h2>
      <div className="button-container">
        <button 
          onClick={handleInitialize} 
          disabled={loading}
          className="database-button"
        >
          {loading ? 'Initializing...' : 'Initialize Database'}
        </button>
        <button 
          onClick={handleLoadData} 
          disabled={loading}
          className="database-button"
        >
          {loading ? 'Loading...' : 'Load Data'}
        </button>
      </div>
      {error && <div className="error-message">{error}</div>}
      {loading && <div className="loading-indicator">Processing...</div>}
    </div>
  );
};

