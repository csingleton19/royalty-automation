// components/Navigation.tsx
import React from 'react';
import { Link } from 'react-router-dom';

export const Navigation: React.FC = () => {
  return (
    <nav>
      <ul>
        <li><Link to="/instructions">Instructions</Link></li>
        <li><Link to="/upload">PDF Upload</Link></li>
        <li><Link to="/database">Database Management</Link></li>
        <li><Link to="/vector-db">Vector DB Management</Link></li>
        <li><Link to="/query">Query Interface</Link></li>

      </ul>
    </nav>
  );
};