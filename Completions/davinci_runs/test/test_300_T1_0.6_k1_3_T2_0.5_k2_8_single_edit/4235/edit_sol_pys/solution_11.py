#!/usr/bin/ruby

# file.rb

class File
  def self.open_and_process(*args)
    f = File.open(*args)
    yield f
    f.close()
  end
end

File.open_and_process("file.rb", "r") do |file|
  while line = file.gets
    puts line
  end
end
