export default class Airport {
  constructor(name, code) {
    this.name = name;
    this.code = code;
  }

  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof this.name !== 'string') {
      throw new TypeError('name must be a string');
    }
    this._name = value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    if (typeof code !== 'string') {
      throw new TypeError('code must be a string');
    }
    this._code = value;
  }

  get [Symbol.toStringTag]() {
    return this._code;
  }
}
