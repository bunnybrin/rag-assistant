export class TaskQueue {
  constructor(delay = 200) {
    this.delay = delay;
    this.queue = [];
    this.isRunning = false;
  }

  push(fn) {
    this.queue.push(fn);
    this.run();
  }

  async run() {
    if (this.isRunning) return;
    this.isRunning = true;

    while (this.queue.length > 0) {
      const task = this.queue.shift();
      await task();
      await new Promise(res => setTimeout(res, this.delay));
    }

    this.isRunning = false;
  }
}

const q = new TaskQueue(1000);

