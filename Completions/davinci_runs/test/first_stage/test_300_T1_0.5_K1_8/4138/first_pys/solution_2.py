

import sys
import time

class Problem:
    def __init__(self, inp, out):
        self.input = inp
        self.output = out
        self.blockSize = [1]
        self.blockDigits = [1]
        self.blockStart = [1]
        self.blockEnd = [1]
        self.blockDigitsSum = [1]
        self.blockStartSum = [1]
        self.blockEndSum = [1]
        self.blockDigitsSumSq = [1]
        self.blockStartSumSq = [1]
        self.blockEndSumSq = [1]
        self.blockDigitsSumSqrt = [1]
        self.blockStartSumSqrt = [1]
        self.blockEndSumSqrt = [1]
        self.blockDigitsSumSqrtSq = [1]
        self.blockStartSumSqrtSq = [1]
        self.blockEndSumSqrtSq = [1]
    
    def solve(self):
        inp = self.input
        out = self.output
        q = int(inp.readline())
        for i in range(q):
            k = int(inp.readline())
            ans = self.getDigitAt(k)
            out.write(str(ans) + "\n")
    
    def getDigitAt(self, k):
        if k == 1:
            return 1
        if self.getBlockId(k) == len(self.blockSize):
            self.growBlock()
        return self.findDigit(k)
    
    def getBlockId(self, k):
        l = 0
        r = len(self.blockSize)
        while l + 1 < r:
            m = (l + r) // 2
            if self.blockEnd[m] < k:
                l = m
            else:
                r = m
        return l
    
    def growBlock(self):
        b = len(self.blockSize)
        self.blockSize.append(self.blockSize[-1] + b + 1)
        self.blockDigits.append(self.blockDigits[-1] + b + 1)
        self.blockStart.append(self.blockEnd[-1] + 1)
        self.blockEnd.append(self.blockEnd[-1] + self.blockSize[-1])
        self.blockDigitsSum.append(self.blockDigitsSum[-1] + self.blockDigits[-1])
        self.blockStartSum.append(self.blockStartSum[-1] + self.blockStart[-1])
        self.blockEndSum.append(self.blockEndSum[-1] + self.blockEnd[-1])
        self.blockDigitsSumSq.append(self.blockDigitsSumSq[-1] + self.blockDigitsSum[-1] * self.blockDigitsSum[-1])
        self.blockStartSumSq.append(self.blockStartSumSq[-1] + self.blockStartSum[-1] * self.blockStartSum[-1])
        self.blockEndSumSq.append(self.blockEndSumSq[-1] + self.blockEndSum[-1] * self.blockEndSum[-1])
        self.blockDigitsSumSqrt.append(self.blockDigitsSumSqrt[-1] + self.blockDigitsSum[-1] ** 0.5)
        self.blockStartSumSqrt.append(self.blockStartSumSqrt[-1] + self.blockStartSum[-1] ** 0.5)
        self.blockEndSumSqrt.append(self.blockEndSumSqrt[-1] + self.blockEndSum[-1] ** 0.5)
        self.blockDigitsSumSqrtSq.append(self.blockDigitsSumSqrtSq[-1] + self.blockDigitsSumSqrt[-1] * self.blockDigitsSumSqrt[-1])
        self.blockStartSumSqrtSq.append(self.blockStartSumSqrtSq[-1] + self.blockStartSumSqrt[-1] * self.blockStartSumSqrt[-1])
        self.blockEndSumSqrtSq.append(self.blockEndSumSqrtSq[-1] + self.blockEndSumSqrt[-1] * self.blockEndSumSqrt[-1])
    
    def findDigit(self, k):
        b = self.getBlockId(k)
        if b == 0:
            return 1
        a = self.blockStart[b]
        x = k - a + 1
        if x <= self.blockSize[b] // 2:
            return self.findDigit1(x, b)
        else:
            return self.findDigit2(x, b)
    
    def findDigit1(self, x, b):
        l = 1
        r = b - 1
        while l + 1 < r:
            m = (l + r) // 2
            if self.blockDigitsSum[m] < x:
                l = m
            else:
                r = m
        return l + 1
    
    def findDigit2(self, x, b):
        l = 1
        r = b - 1
        while l + 1 < r:
            m = (l + r) // 2
            if self.blockStartSum[m] < x:
                l = m
            else:
                r = m
        return r + 1

start = time.time()
inp = sys.stdin
out = sys.stdout
Problem(inp, out).solve()
end = time.time()
print(end - start)