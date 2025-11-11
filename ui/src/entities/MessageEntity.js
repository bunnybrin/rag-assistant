import { SourceEntity } from './SourceEntity';

export class MessageEntity {
  constructor(data) {
    this.id = data.id || Date.now().toString();
    this.type = data.type;
    this.content = data.content || '';
    this.sources = data.sources ? SourceEntity.fromArray(data.sources) : [];
    this.timestamp = data.timestamp || new Date();
    this.isLoading = data.isLoading || false;
    this.error = data.error || null;
  }

  get isUser() {
    return this.type === 'user';
  }

  get isBot() {
    return this.type === 'bot';
  }

  get formattedTime() {
    const date = new Date(this.timestamp);
    return date.toLocaleTimeString('uk-UA', { hour: '2-digit', minute: '2-digit' });
  }

  static createUserMessage(content) {
    return new MessageEntity({
      type: 'user',
      content,
      timestamp: new Date(),
    });
  }

  static createBotMessage(content, sources = []) {
    return new MessageEntity({
      type: 'bot',
      content,
      sources,
      timestamp: new Date(),
    });
  }

  static createLoadingMessage() {
    return new MessageEntity({
      type: 'bot',
      content: '',
      isLoading: true,
      timestamp: new Date(),
    });
  }
}
