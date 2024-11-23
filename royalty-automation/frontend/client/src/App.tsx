// src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { PdfUploader } from './components/PDFUploader';
import { Navigate } from 'react-router-dom';
import { DatabaseManager } from './components/DatabaseManager';
import { QueryInterface } from './components/QueryInterface';
import { VectorDBManager } from './components/VectorDBManager';
import { Navigation } from './components/Navigation';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        {/* Redirect root to upload page */}
        <Route path="/" element={<Navigate to="/upload" />} />
        
        {/* Existing route */}
        <Route path="/upload" element={<PdfUploader />} />
        
        {/* New routes */}
        <Route path="/database" element={<DatabaseManager />} />
        <Route path="/query" element={<QueryInterface />} />
        <Route path="/vector-db" element={<VectorDBManager />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;