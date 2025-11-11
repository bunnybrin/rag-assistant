class ChatApp {
    constructor() {
        this.sessionId = null;
        this.ws = null;
        this.isConnected = false;

        this.chatArea = document.getElementById('chatArea');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.statusElement = document.getElementById('status');

        this.init();
    }

    async init() {
        this.setupWebSocket();
        this.setupEventListeners();
    }

    setupWebSocket() {
        const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
        const wsUrl = `${protocol}//${window.location.host}/api/ws/chat`;

        this.ws = new WebSocket(wsUrl);

        this.ws.onopen = () => {
            console.log('WebSocket connected');
            this.isConnected = true;
            this.updateStatus('⏳ Очікування sessionId...');
        };

        this.ws.onclose = () => {
            console.log('WebSocket disconnected');
            this.isConnected = false;
            this.updateStatus('❌ Відключено');
        };

        this.ws.onerror = (error) => {
            console.error('WebSocket error:', error);
            this.updateStatus('❌ Помилка підключення');
        };

        this.ws.onmessage = (event) => {
            this.handleWebSocketMessage(event.data);
        };
    }

    handleWebSocketMessage(data) {
        const message = JSON.parse(data);

        switch (message.type) {
            case 'session':
                this.sessionId = message.session_id;
                console.log('Session ID отримано:', this.sessionId);
                this.updateStatus('✅ Підключено');
                break;

            case 'start':
                // this.showTypingIndicator();
                break;

            case 'stream':
                // this.appendToLastMessage(message.content);
                break;

            case 'end':
                this.hideTypingIndicator();
                this.appendToLastMessage(message.content);
                if (message.sources && message.sources.length > 0) {
                    this.showSources(message.sources);
                }
                this.scrollToBottom();
                break;

            case 'error':
                this.hideTypingIndicator();
                this.showError(message.message);
                break;
        }
    }

    setupEventListeners() {
        this.sendButton.addEventListener('click', () => this.sendMessage());

        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });
    }

    async sendMessage() {
        const message = this.messageInput.value.trim();

        if (!message || !this.isConnected) {
            return;
        }

        this.addMessage('user', message);
        this.messageInput.value = '';
        this.sendButton.disabled = true;

        this.ws.send(JSON.stringify({ message }));

        this.showTypingIndicator();
        // this.currentAssistantMessage = this.createMessageElement('assistant', '');
        // this.chatArea.appendChild(this.currentAssistantMessage);

        setTimeout(() => {
            this.sendButton.disabled = false;
            this.messageInput.focus();
        }, 500);
    }

    addMessage(role, content) {
        const messageDiv = this.createMessageElement(role, content);
        this.chatArea.appendChild(messageDiv);
        this.scrollToBottom();
    }

    createMessageElement(role, content) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        contentDiv.textContent = content;

        messageDiv.appendChild(contentDiv);

        return messageDiv;
    }

    appendToLastMessage(text) {
        if (!this.currentAssistantMessage) {
            this.currentAssistantMessage = this.createMessageElement('assistant', '');
            this.chatArea.appendChild(this.currentAssistantMessage);
        }

        const contentDiv = this.currentAssistantMessage.querySelector('.message-content');
        contentDiv.textContent += text;

        this.scrollToBottom();
    }

    showSources(sources) {
        if (!this.currentAssistantMessage) return;

        const sourcesDiv = document.createElement('div');
        sourcesDiv.className = 'sources';

        const title = document.createElement('div');
        title.className = 'sources-title';
        title.textContent = '📚 Джерела:';
        sourcesDiv.appendChild(title);

        sources.forEach(source => {
            const sourceItem = document.createElement('div');
            sourceItem.className = 'source-item';

            const fileName = source.metadata.file_name || 'Unknown';
            const page = source.metadata.page_label || '';
            const score = source.score ? ` (релевантність: ${source.score.toFixed(2)})` : '';

            sourceItem.textContent = `• ${fileName}${page ? ` - сторінка ${page}` : ''}${score}`;
            sourcesDiv.appendChild(sourceItem);
        });

        this.currentAssistantMessage.appendChild(sourcesDiv);
        this.scrollToBottom();
    }

    showTypingIndicator() {
        if (!this.typingIndicator) {
            this.typingIndicator = document.createElement('div');
            this.typingIndicator.className = 'message assistant';
            this.typingIndicator.innerHTML = `
                <div class="typing-indicator active">
                    <span></span>
                    <span></span>
                    <span></span>
                </div>
            `;
        }
        this.chatArea.appendChild(this.typingIndicator);
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        if (this.typingIndicator && this.typingIndicator.parentNode) {
            this.typingIndicator.parentNode.removeChild(this.typingIndicator);
        }
    }

    showError(message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error';
        errorDiv.textContent = `❌ ${message}`;
        this.chatArea.appendChild(errorDiv);
        this.scrollToBottom();
    }

    updateStatus(status) {
        this.statusElement.textContent = status;
    }

    scrollToBottom() {
        this.chatArea.scrollTop = this.chatArea.scrollHeight;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new ChatApp();
});
