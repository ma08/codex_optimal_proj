# Reverse bits of a given 32 bits unsigned integer.

# Example 1:

# Input: 00000010100101000001111010011100
# Output: 00111001011110000010100101000000
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
# Example 2:

# Input: 11111111111111111111111111111101
# Output: 10111111111111111111111111111111
# Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.




class Solution:
    def reverseBits(self, n: int) -> int:
        # n is binary string of length 32
        bin_str = bin(n)[2:]
        bin_str = bin_str.zfill(32)
        bin_str = bin_str[::-1]
        return int(bin_str, 2)
