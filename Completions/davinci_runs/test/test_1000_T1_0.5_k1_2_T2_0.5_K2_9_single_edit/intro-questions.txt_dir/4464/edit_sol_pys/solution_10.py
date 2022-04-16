def gcd(a, b)
  return a if b == 0
  gcd(b, a % b)
end

a, b, c = gets.split.map(&:to_i)

if c % gcd(a, b) == 0 && c <= a * b
  puts 'YES'
else
  puts 'NO'
end
