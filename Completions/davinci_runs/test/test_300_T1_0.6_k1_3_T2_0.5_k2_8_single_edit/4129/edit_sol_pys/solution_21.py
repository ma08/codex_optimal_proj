require 'fileutils'

class File
  def self.write(file, content)
    FileUtils.mkdir_p File.dirname(file)
    File.open(file, 'w') { |f| f.write content }
  end
end
