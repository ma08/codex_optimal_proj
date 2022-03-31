#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import time
import random
import string
import hashlib
import logging
import traceback

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.escape

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=False, help="run in debug mode")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/upload", UploadHandler),
            (r"/download", DownloadHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            debug=options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")

class UploadHandler(BaseHandler):
    def post(self):
        try:
            file_name = self.get_argument("file_name")
            file_data = self.get_argument("file_data")
            file_data = file_data.replace("data:application/octet-stream;base64,", "")
            file_data = file_data.decode("base64")
            file_path = os.path.join(os.path.dirname(__file__), "upload", file_name)
            with open(file_path, "wb") as f:
                f.write(file_data)
            self.write({"status": "success"})
        except:
            logging.error(traceback.format_exc())
            self.write({"status": "fail"})

class DownloadHandler(BaseHandler):
    def get(self):
        try:
            file_name = self.get_argument("file_name")
            file_path = os.path.join(os.path.dirname(__file__), "upload", file_name)
            with open(file_path, "rb") as f:
                file_data = f.read()
            self.write({"status": "success", "file_data": file_data.encode("base64")})
        except:
            logging.error(traceback.format_exc())
            self.write({"status": "fail"})

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
