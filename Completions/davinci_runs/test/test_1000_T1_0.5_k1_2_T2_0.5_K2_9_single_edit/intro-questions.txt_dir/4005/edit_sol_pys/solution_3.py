#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
#  
#  Copyright 2014 Balint Seeber <balint256@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import time

class FileWriter(object):
	def __init__(self, filename):
		self.filename = filename
		self.file = open(filename, 'wb')
		self.start_time = time.time()
		self.last_time = self.start_time
		self.last_bytes = 0
	def __del__(self):
		self.close()
	def close(self):
		self.file.close()
	def write(self, data):
		self.file.write(data)
		self.last_time = time.time()
		self.last_bytes += len(data)
	def get_rate(self):
		if self.last_time == self.start_time:
			return 0
		return self.last_bytes / (self.last_time - self.start_time)
	def get_elapsed_time(self):
		return self.last_time - self.start_time

def main():
	return 0

if __name__ == '__main__':
	main()
