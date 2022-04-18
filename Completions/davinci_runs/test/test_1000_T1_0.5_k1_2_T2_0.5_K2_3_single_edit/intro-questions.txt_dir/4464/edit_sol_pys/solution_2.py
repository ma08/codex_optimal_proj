def gcd(a, b)
  if b == 0
    a
  else
    gcd(b, a % b)
  end
end


# a, b, c = gets.split.map(&:to_i)
a, b, c = 7, 2, 6

if c % gcd(a, b) == 0
  puts 'YES'
else
  puts 'NO'
end
