const mongoose = require('mongoose');
const Schema = mongoose.Schema;

let File = new Schema({
    file_description: {
        type: String
    },
    file_responsible: {
        type: String
    },
    file_priority: {
        type: String
    },
    file_completed: {
        type: Boolean
    }
});

module.exports = mongoose.model('File', File);
