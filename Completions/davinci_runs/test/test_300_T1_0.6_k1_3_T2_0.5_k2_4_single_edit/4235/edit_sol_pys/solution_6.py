class File
  def self.read_file(file)
    file = File.open(file, "r")

    while !file.eof?
      puts file.gets
    end
  end

  def self.write_file(file, string)
    file = File.open(file, "a")
    file.puts string
    file.close
  end
end

File.read_file("file.rb")
File.write_file("file.rb", "puts 'hello'")
