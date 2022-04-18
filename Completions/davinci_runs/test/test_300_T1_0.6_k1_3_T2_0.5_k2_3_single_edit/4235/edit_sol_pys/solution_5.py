const { readFile } = require('fs')
const { promisify } = require('util')

const readFileAsync = promisify(readFile)

class File {
    constructor(file) {
        this.file = file
    }

    async getFileAsString() {
        try {
            if (this.file == null) throw 'No file path provided'
            const data = await readFileAsync(this.file, 'utf8')
            return data
        } catch (err) {
            console.error(err)
            return err
        }
    }

    async getFileAsJSON() {
        try {
            if (this.file == null) throw 'No file path provided'
            const data = await readFileAsync(this.file, 'utf8')
            const json = JSON.parse(data)
            return json
        } catch (err) {
            console.error(err)
            return err
        }
    }

    async saveStringToFile(text) {
        try {
            if (this.file == null) throw 'No file path provided'
            if (text == null) throw 'No text provided'
            const json = JSON.stringify(text)
            await writeFileAsync(this.file, json)
            return true
        } catch (err) {
            console.error(err)
            return err
        }
    }

    async saveJSONToFile(obj) {
        try {
            if (this.file == null) throw 'No file path provided'
            if (obj == null) throw 'No object provided'
            const json = JSON.stringify(obj)
            await writeFileAsync(this.file, json)
            return true
        } catch (err) {
            console.error(err)
            return err
        }
    }
}

module.exports = File
