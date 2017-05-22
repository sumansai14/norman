import $ from 'jquery';
import _ from 'underscore';

export class Request {
  constructor(xhr) {
    this.xhr = xhr;
    this.alive = true;
  }

  cancel() {
    this.alive = false;
    this.xhr.abort();
  }
}

export class Client {
    
    constructor(options) {
        if (_.isUndefined(options)) {
          options = {};
        }
        this.baseUrl = options.baseUrl || '/api/0';
        this.activeRequests = {};
    }

    clear() {
        for (let id in this.activeRequests) {
            this.activeRequests[id].cancel();
        }
    }
}