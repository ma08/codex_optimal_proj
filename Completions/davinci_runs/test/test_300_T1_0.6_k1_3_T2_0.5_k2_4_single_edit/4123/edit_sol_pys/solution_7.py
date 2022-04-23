/*
 *  file.js
 *
 *  David Janes
 *  IOTDB.org
 *  2016-01-03
 *
 *  Copyright [2013-2016] [David P. Janes]
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

"use strict";

const iotdb = require('iotdb');
const _ = iotdb._;

const fs = require('fs');
const path = require('path');

const assert = require("assert");
const thing = require("../thing");

const model_file = require('./models/file');

describe("file", function() {
    describe("file", function() {
        it("file", function(done) {
            const thing_1 = thing.make({
                model: model_file,
                file: path.join(__dirname, "data", "file", "file.txt"),
            });

            thing_1.on("istate", function(thing) {
                const istate = thing.state("istate");

                assert.ok(_.is.Buffer(istate.file));
                assert.ok(Buffer.compare(istate.file, new Buffer("Hello, World")) === 0);

                done();
            });
        });
    });
});
