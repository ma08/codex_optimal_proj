class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit



# class Solution:
#     def canThreePartsEqualSum(self, A) -> bool:
#         total = sum(A)
#         if total % 3 != 0:
#             return False
#         part_sum = total // 3
#         i, cur_sum = 0, 0
#         while i < len(A):
#             cur_sum += A[i]
#             if cur_sum == part_sum:
#                 break
#             i += 1
#         if cur_sum != part_sum:
#             return False
#         j, cur_sum = i + 1, 0
#         while j < len(A):
#             cur_sum += A[j]
#             if cur_sum == part_sum:
#                 break
#             j += 1
#         if cur_sum != part_sum:
#             return False
#         return True


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
