
def celsius_to_fahrenheit(celsius):
   return (celsius*1.8)+32
def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit-32)/1.8
#-----Solution-----

print(celsius_to_fahrenheit(0))
print(fahrenheit_to_celsius(32))
print(fahrenheit_to_celsius(celsius_to_fahrenheit(0)))
print(celsius_to_fahrenheit(fahrenheit_to_celsius(32)))
#-----Test-----
