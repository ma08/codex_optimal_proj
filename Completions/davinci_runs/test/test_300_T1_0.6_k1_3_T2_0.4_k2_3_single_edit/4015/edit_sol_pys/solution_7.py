def read_file_to_array(file_name)
  file_contents = []
  File.open(file_name, 'r') do |file|
    file.each_line do |line|
      file_contents << line
    end
  end
  file_contents
end

def write_array_to_file(file_name, array)
  File.open(file_name, 'w') do |file|
    array.each do |element|
      file.puts(element)
    end
  end
end

def delete_file(file_name)
  File.delete(file_name)
end

def file_exists?(file_name)
  File.exist?(file_name)
end

def file_size(file_name)
  File.size(file_name)
end

def file_mtime(file_name)
  File.mtime(file_name)
end

def file_atime(file_name)
  File.atime(file_name)
end
