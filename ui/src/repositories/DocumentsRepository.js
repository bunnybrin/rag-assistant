import {http} from '../api/axios';
import {DocumentsEntity} from "../entities/DocumentsEntity.js";

export class DocumentsRepository {
  static async getDocuments() {
    const response = await http.get('/api/pipelines');
    
    return DocumentsEntity.fromArray(response.data)
  }
  
  
  static async previewDocuments(id) {
    const response = await http.get(`/api/files/${id}`);
    
    return {
      url: response.data,
    }
   
  }
}
