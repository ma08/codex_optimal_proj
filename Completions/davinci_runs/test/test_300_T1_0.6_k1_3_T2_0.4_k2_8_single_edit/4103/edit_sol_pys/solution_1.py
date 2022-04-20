
# import sys
#
# def main():
#     n, b, a = [int(i) for i in sys.stdin.readline().strip().split(' ')]
#     s = [int(i) for i in sys.stdin.readline().strip().split(' ')]
#     b_left = b
#     a_left = a
#
#     max_segments = 0
#     i = 0
#     while i < n:
#         if b_left == 0:
#             if a_left > 0:
#                 a_left -= 1
#                 max_segments += 1
#             else:
#                 break
#         elif a_left == 0:
#             if b_left > 0:
#                 b_left -= 1
#                 max_segments += 1
#             else:
#                 break
#         elif s[i] == 1:
#             if a_left < a:
#                 a_left += 1
#                 b_left -= 1
#                 max_segments += 1
#             elif b_left > 0:
#                 b_left -= 1
#                 max_segments += 1
#             else:
#                 break
#         elif s[i] == 0:
#             if a_left > 0:
#                 a_left -= 1
#                 max_segments += 1
#             elif b_left > 0:
#                 b_left -= 1
#                 max_segments += 1
#             else:
#                 break
#         i += 1
#     print(max_segments)
#
# main()
