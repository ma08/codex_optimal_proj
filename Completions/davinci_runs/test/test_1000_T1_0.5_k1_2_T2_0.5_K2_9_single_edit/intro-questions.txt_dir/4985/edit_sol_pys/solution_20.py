

# N, B = input().split()
# N = int(N)

# cards = []
# for i in range(N*4):
#     cards.append(input().split())

# dominant = ['S', 'H', 'D', 'C']
# dominant.remove(B)

# points = 0
# for card in cards:
#     if card[1] == B:
#         if card[0] == 'A':
#             points += 11
#         elif card[0] == 'K':
#             points += 4
#         elif card[0] == 'Q':
#             points += 3
#         elif card[0] == 'J':
#             points += 20
#         elif card[0] == 'T':
#             points += 10
#         elif card[0] == '9':
#             points += 14
#     elif card[1] in dominant:
#         if card[0] == 'A':
#             points += 11
#         elif card[0] == 'K':
#             points += 4
#         elif card[0] == 'Q':
#             points += 3
#         elif card[0] == 'J':
#             points += 2
#         elif card[0] == 'T':
#             points += 10

# print(points)
