class SourceItem {
  constructor(sourceData, index) {
    const node = sourceData.node || {};
    const metadata = node.metadata || {};

    this.id = node.id_ || '';
    this.index = index + 1;
    this.score = sourceData.score || 0;
    this.text = node.text || '';
    this.preview = this.text.substring(0, 200);
    this.metadata = {
      id: metadata.id || '',
      fileSize: metadata.file_size || 0,
      lastModifiedAt: metadata.last_modified_at || '',
      filePath: metadata.file_path || '',
      fileName: metadata.file_name || '',
      externalFileId: metadata.external_file_id || '',
      fileId: metadata.file_id || '',
      pipelineFileId: metadata.pipeline_file_id || '',
      pipelineId: metadata.pipeline_id || '',
      pageLabel: metadata.page_label || 0,
      startPageIndex: metadata.start_page_index || 0,
      startPageLabel: metadata.start_page_label || 0,
      endPageIndex: metadata.end_page_index || 0,
      endPageLabel: metadata.end_page_label || 0,
      documentId: metadata.document_id || '',
      startCharIdx: metadata.start_char_idx || 0,
      endCharIdx: metadata.end_char_idx || 0,
      fileType: this._getFileType(metadata.file_name || ''),
      lastModifiedDate: metadata.last_modified_at || ''
    };
  }

  _getFileType(fileName) {
    const ext = fileName.split('.').pop()?.toUpperCase() || '';
    return ext ? `.${ext}` : 'Unknown';
  }

  get formattedFileSize() {
    const bytes = this.metadata.fileSize;
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return Math.round((bytes / Math.pow(k, i)) * 100) / 100 + ' ' + sizes[i];
  }

  get formattedScore() {
    return this.score !== null ? (this.score * 100).toFixed(1) + '%' : 'N/A';
  }
}

export class ChatResponseEntity {
  constructor(data) {
    this.type = data.type || 'end';
    this.content = data.content || '';
    this.sources = this._convertSources(data.sources || []);
    this.sessionId = data.session_id || '';
  }

  _convertSources(sources) {
    return sources.map((source, index) => new SourceItem(source, index));
  }

  static create(data) {
    return new ChatResponseEntity(data);
  }
}
