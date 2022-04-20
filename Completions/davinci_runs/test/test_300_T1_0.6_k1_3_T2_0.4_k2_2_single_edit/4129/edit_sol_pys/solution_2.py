#!/usr/bin/env ruby

#
# This script is used to detect the type of a file.
#
# Usage:
#
#   file.rb <file>
#
# Example:
#
#   file.rb test.txt
#

require 'filemagic'

def usage
  puts "Usage: #{$0} <file>"
  exit 1
end

usage if ARGV.empty?

filename = ARGV.first

if File.exist?(filename)
  mime = FileMagic.new(FileMagic::MAGIC_MIME)
  puts mime.file(filename)
else
  puts "File '#{filename}' does not exist."
end
