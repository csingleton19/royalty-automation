// src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { PdfUploader } from './components/PDFUploader';
import { Navigate } from 'react-router-dom';
import { DatabaseManager } from './components/DatabaseManager';
import { QueryInterface } from './components/QueryInterface';
import { VectorDBManager } from './components/VectorDBManager';
import { Navigation } from './components/Navigation';
import { Instructions } from './components/Instructions';
import './App.css';

function App() {
  return (
    <BrowserRouter>
      <Navigation />
      <Routes>
        {/* Changed redirect to instructions */}
        <Route path="/" element={<Navigate to="/instructions" />} />
        
        <Route path="/instructions" element={<Instructions />} />
        <Route path="/upload" element={<PdfUploader />} />
        <Route path="/database" element={<DatabaseManager />} />
        <Route path="/query" element={<QueryInterface />} />
        <Route path="/vector-db" element={<VectorDBManager />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;