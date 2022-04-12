a, b, c = gets.split.map(&:to_i)

if c % a.gcd(b) == 0
  puts 'YES'
else
  puts 'NO'
end
