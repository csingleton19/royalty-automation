// src/App.tsx
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { PdfUploader } from './components/PdfUploader';
// Import other components

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/upload" element={<PdfUploader />} />
        {/* Add other routes */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;