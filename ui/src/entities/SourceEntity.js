export class SourceEntity {
  constructor(data) {
    this.id = data.id;
    this.index = data.index;
    this.score = data.score;
    this.text = data.text;
    this.preview = data.preview;
    this.metadata = {
      fileName: data.metadata?.file_name || '',
      filePath: data.metadata?.file_path || '',
      fileType: data.metadata?.file_type || '',
      pageLabel: data.metadata?.page_label || '',
      fileSize: data.metadata?.file_size || 0,
      lastModifiedDate: data.metadata?.last_modified_date || '',
    };
    this.position = data.position || null;
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

  static fromArray(sources) {
    if (!Array.isArray(sources)) return [];
    return sources.map(source => new SourceEntity(source));
  }
}
