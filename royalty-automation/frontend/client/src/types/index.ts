// src/types/index.ts
export interface QueryResponse {
    // define response structure
    results: any;
    message?: string;
  }
  
  export interface ExtractPdfResponse {
    // define response structure
    success: boolean;
    data?: any;
    error?: string;
  }