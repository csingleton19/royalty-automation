// components/QueryInterface.tsx
import React, { useState } from 'react';
import { api } from '../services/api';

export const QueryInterface: React.FC = () => {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<any>(null);
  const [error, setError] = useState<string | null>(null);

  const handleQuery = async () => {
    setLoading(true);
    try {
      const response = await api.processQuery(query);
      setResult(response.data);
    } catch (err) {
      setError('Failed to process query');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Query Interface</h2>
      <textarea 
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Enter your query here"
      />
      <button onClick={handleQuery} disabled={loading}>
        Submit Query
      </button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
      {error && <div className="error">{error}</div>}
    </div>
  );
};

