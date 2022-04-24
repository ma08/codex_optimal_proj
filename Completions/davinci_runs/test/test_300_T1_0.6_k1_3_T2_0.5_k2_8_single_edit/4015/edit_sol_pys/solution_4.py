def open_file(filename)
  file = File.open(filename)
  yield file
  file.close
end

open_file('test.txt') do |file|
  puts file.read
end
