

a, b, c = gets.split.map(&:to_i)

if c % [a, b].reduce(:gcd) == 0
  puts 'YES'
else
  puts 'NO'
end
