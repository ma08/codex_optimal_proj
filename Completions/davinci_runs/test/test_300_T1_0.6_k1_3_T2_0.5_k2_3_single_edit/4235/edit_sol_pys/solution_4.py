#!/usr/bin/env ruby

require 'optparse'

options = {}
OptionParser.new do |opts|
  opts.banner = "Usage: file.rb [options]"

  opts.on('-t', '--target TARGET', 'Target Directory') do |t|
    options[:target] = t
  end

  opts.on('-s', '--source SOURCE', 'Source Directory') do |s|
    options[:source] = s
  end
end.parse!

puts options
