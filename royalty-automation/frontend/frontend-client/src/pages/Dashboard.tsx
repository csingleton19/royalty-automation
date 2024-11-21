// frontend-client/src/pages/Dashboard.tsx
import React from 'react';
import { PDFUploader } from '../components/PDFUploader';

export const Dashboard: React.FC = () => {
  return (
    <div>
      <h1>Document Processing Dashboard</h1>
      <PDFUploader />
      {/* Add other components */}
    </div>
  );
};