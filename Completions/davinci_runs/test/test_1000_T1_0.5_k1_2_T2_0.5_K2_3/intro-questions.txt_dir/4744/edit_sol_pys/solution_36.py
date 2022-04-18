
import math

class Solution:

    def __init__(self, volume):
        self.volume = volume
        self.cost = math.inf
    
    def find_cost(self):
        for i in range(1, int(math.sqrt(self.volume)) + 1):
            if self.volume % i == 0:
                if 2 * i + 2 * (self.volume // i) < self.cost:
                    self.cost = 2 * i + 2 * (self.volume // i)
        return self.cost

volume = int(input())
s = Solution(volume)
print(s.find_cost())
