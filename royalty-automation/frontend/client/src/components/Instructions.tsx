import React from 'react';

export const Instructions: React.FC = () => {
  return (
    <div>
      <h2>How to Use This Application</h2>
      <ol>
        <li>
          <h3>Step 1: Upload PDF Files</h3>
          <p>Navigate to the Upload page and select your PDF files containing royalty information.</p>
        </li>
        <li>
          <h3>Step 2: Initialize Database</h3>
          <p>Go to Database Management to initialize the database structure.</p>
        </li>
        <li>
          <h3>Step 3: Vector Database Setup</h3>
          <p>Use the Vector DB page to upload and process embeddings.</p>
        </li>
        <li>
          <h3>Step 4: Query Your Data</h3>
          <p>Finally, use the Query Interface to search and analyze your royalty data.</p>
        </li>
      </ol>
    </div>
  );
};