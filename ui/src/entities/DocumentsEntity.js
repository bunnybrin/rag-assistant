import {formatFileSize} from "../utils/fileSize.js";

export class DocumentEntity {
  constructor(document) {
    this.text = document.text
    this.id = document.metadata.file_id
    this.name = document.metadata.file_name
    this.pipleneId = document.id
    this.status = document['status_metadata'].status
    this.error = document['status_metadata'].error
    this._fileSize = document.metadata.file_size
  }
  
  get fileType() {
    return this.name.split('.')[1]
  }
  
  get fileSize() {
    return formatFileSize(this._fileSize)
  }
  
  static create(documents) {
    return new DocumentEntity(documents)
  }
}


export class DocumentsEntity {
  constructor(documents) {
    this.documents = documents
  }
  
  static fromArray(documents) {
    return new DocumentsEntity(documents.map(doc => DocumentEntity.create(doc)))
  }
}
