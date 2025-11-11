import {http} from '../api/axios';

export class DocumentsRepository {
  static async getDocuments() {
    const response = await http.get('/api/documents');
    return response.data;
  }
  
  static async getDocumentsCount() {
    const response = await http.get('/api/documents/count');
    return response.data;
  }
  
  static async downloadDocument(fileName) {
    const response = await http.get(`/api/documents/download/${fileName}`, {
      responseType: 'blob',
    });
    return response.data;
  }
}
