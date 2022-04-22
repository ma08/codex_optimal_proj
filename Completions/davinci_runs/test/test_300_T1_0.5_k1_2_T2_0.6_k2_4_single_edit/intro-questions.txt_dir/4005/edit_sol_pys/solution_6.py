require 'csv'

CSV.foreach('/Users/drew/Desktop/file.csv') do |row|
  puts "#{row[0]}, #{row[1]}"
end





