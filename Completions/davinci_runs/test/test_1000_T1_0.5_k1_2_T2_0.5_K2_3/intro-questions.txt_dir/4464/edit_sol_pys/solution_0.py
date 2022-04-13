
def gcd(a, b)
  a, b = b, a % b while b != 0
  a
end
a, b, c = gets.split.map(&:to_i)

if c % gcd(a, b) == 0
  puts 'YES'
else
  puts 'NO'
end
