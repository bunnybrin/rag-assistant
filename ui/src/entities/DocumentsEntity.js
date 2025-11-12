export class DocumentEntity {
  constructor(document) {
    this.text = document.text
    this.id = document.metadata.file_id
    this.name = document.metadata.file_name
    this.pipleneId = document.id
    this.status = document['status_metadata'].status
    this.error = document['status_metadata'].error
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
