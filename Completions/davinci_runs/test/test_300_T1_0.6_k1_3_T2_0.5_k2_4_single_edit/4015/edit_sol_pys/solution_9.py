#!/usr/bin/python
# -*- coding: UTF-8 -*-

class File:
	def __init__(self, name):
		self.name = name
		self.size = 0
		self.contents = ""
		self.children = []
		self.parent = None

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.__str__()

	def add_child(self, child):
		self.children.append(child)
		child.parent = self

	def get_size(self):
		if self.size == 0 and len(self.children) > 0:
			self.size = sum([child.get_size() for child in self.children])
		return self.size

	def get_path(self):
		if self.parent == None:
			return "/"
		else:
			return self.parent.get_path() + self.name + "/"

	def get_contents(self):
		if self.contents == "" and len(self.children) > 0:
			self.contents = "".join([child.get_contents() for child in self.children])
		return self.contents

	def get_parent(self):
		return self.parent

	def get_children(self):
		return self.children

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.name = name

	def set_size(self, size):
		self.size = size

	def set_contents(self, contents):
		self.contents = contents

	def set_parent(self, parent):
		self.parent = parent

	def set_children(self, children):
		self.children = children
