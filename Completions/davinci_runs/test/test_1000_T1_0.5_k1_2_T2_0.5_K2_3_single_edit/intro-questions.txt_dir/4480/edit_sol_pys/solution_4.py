
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


class Solution:
    def canThreePartsEqualSum(self, A):
        total = sum(A)
        if total % 3 != 0:
            return False
        part_sum, i, cur_sum = total // 3, 0, 0
        for i in range(len(A)):
            cur_sum += A[i]  # 前面的和
            if cur_sum == part_sum:  # 前面的和等于总和的1/3
                break
        if cur_sum != part_sum:  # 前面的和不等于总和的1/3
            return False
        j, cur_sum = i + 1, 0  # 前面的和等于总和的1/3
        for j in range(i + 1, len(A)):
            cur_sum += A[j]
            if cur_sum == part_sum:  # 后面的和等于总和的1/3
                break
        if cur_sum != part_sum:  # 后面的和不等于总和的1/3
            return False
        return True


if __name__ == '__main__':
    A = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    print(Solution().canThreePartsEqualSum(A))
