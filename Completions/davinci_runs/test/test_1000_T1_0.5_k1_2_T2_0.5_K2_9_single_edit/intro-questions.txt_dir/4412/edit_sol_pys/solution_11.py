const fs = require('fs')
const path = require('path')

const getFileByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        fs.readFile(fPath, (err, data) => {
            if (err) {
                reject(err)
            } else {
                resolve(data)
            }
        })
    })
}

const getFileNameList = (fPath) => {
    return new Promise((resolve, reject) => {
        fs.readdir(fPath, (err, files) => {
            if (err) {
                reject(err)
            } else {
                resolve(files)
            }
        })
    })
}

const getFileNameListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        getFileNameList(fPath)
            .then(files => {
                let result = files.map(file => {
                    return path.join(fPath, file)
                })
                resolve(result)
            })
            .catch(err => {
                reject(err)
            })
    })
}

const getFileStat = (fPath) => {
    return new Promise((resolve, reject) => {
        fs.stat(fPath, (err, stats) => {
            if (err) {
                reject(err)
            } else {
                resolve(stats)
            }
        })
    })
}

const getFileStatListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        getFileNameListByPath(fPath)
            .then(files => {
                let promises = files.map(file => {
                    return getFileStat(file)
                })
                Promise.all(promises)
                    .then(stats => {
                        resolve(stats)
                    })
                    .catch(err => {
                        reject(err)
                    })
            })
            .catch(err => {
                reject(err)
            })
    })
}

const getFileListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        getFileStatListByPath(fPath)
            .then(stats => {
                let result = stats.map(stat => {
                    return stat.isFile()
                })
                resolve(result)
            })
            .catch(err => {
                reject(err)
            })
    })
}

const getDirListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        getFileStatListByPath(fPath)
            .then(stats => {
                let result = stats.map(stat => {
                    return stat.isDirectory()
                })
                resolve(result)
            })
            .catch(err => {
                reject(err)
            })
    })
}

const getDirListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        getFileStatListByPath(fPath)
            .then(stats => {
                let result = stats.map(stat => {
                    return stat.isDirectory()
                })
                resolve(result)
            })
            .catch(err => {
                reject(err)
            })
    })
}

const getFileAndDirListByPath = (fPath) => {
    return new Promise((resolve, reject) => {
        Promise.all([getFileListByPath(fPath), getDirListByPath(fPath)])
            .then(results => {
                let files = results[0]
                let dirs = results[1]
                let result = []
                for (let i = 0; i < files.length; i++) {
                    let type = 'file'
                    if (dirs[i]) {
                        type = 'dir'
                    }
                    result.push({
                        name: files[i],
                        type: type
                    })
                }
                resolve(result)
            })
            .catch(err => {
                reject(err)
            })
    })
}

module.exports = {
    getFileByPath,
    getFileNameList,
    getFileNameListByPath,
    getFileStat,
    getFileStatListByPath,
    getFileListByPath,
    getDirListByPath,
    getFileAndDirListByPath
}
