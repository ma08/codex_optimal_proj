File.open('file.txt', 'w') { |f| f.write('Hello World!') }

puts File.read('file.txt')
