

import { createWriteStream } from 'fs';
import { createHash } from 'crypto';

export default class File {
  constructor(name, path, size, type, hash) {
    this.name = name;
    this.path = path;
    this.size = size;
    this.type = type;
    this.hash = hash;
  }

  static async create(file) {
    const { name, path, size, type } = file;
    const hash = await this.hash(file);
    return new File(name, path, size, type, hash);
  }

  static async hash(file) {
    const hash = createHash('sha256');
    const stream = createWriteStream(file.path);
    stream.on('data', (data) => {
      hash.update(data);
    });
    return new Promise((resolve) => {
      stream.on('finish', () => {
        resolve(hash.digest('hex'));
      });
    });
  }
}
