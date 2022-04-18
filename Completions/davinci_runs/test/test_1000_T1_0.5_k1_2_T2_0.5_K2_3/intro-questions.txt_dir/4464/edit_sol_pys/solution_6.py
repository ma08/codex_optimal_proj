

def gcd(a, b)
  if b == 0
    a
  else
    gcd(b, a % b)
  end
end

def lcm(a, b)
  a * b / gcd(a, b)
end
def main
  a, b, c = gets.split.map(&:to_i)

  if c % gcd(a, b) == 0
    puts 'YES'
  else
    puts 'NO'
  end
end

main
