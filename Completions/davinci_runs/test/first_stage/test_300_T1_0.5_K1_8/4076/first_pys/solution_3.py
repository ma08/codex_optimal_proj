

import math

a, b, h, m = map(int, input().split())

h_rad = h * 30 + m / 2
m_rad = m * 6

h_x = a * math.cos(math.radians(h_rad))
h_y = a * math.sin(math.radians(h_rad))
m_x = b * math.cos(math.radians(m_rad))
m_y = b * math.sin(math.radians(m_rad))

distance = math.sqrt((h_x - m_x) ** 2 + (h_y - m_y) ** 2)
print(distance)