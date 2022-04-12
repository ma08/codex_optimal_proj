
#-----main-----#
syllables, players = [int(x) for x in input().split()]

#-----classes-----#
class Player:
    def __init__(self, number):
        self.number = number
        self.hands = [True, False]
        self.out = False

    def spill(self):
        for i in range(2):
            if not self.hands[i]:
                self.hands[i] = True
                break

    def put_out(self):
        if self.hands[0] and self.hands[1]:
            self.hands = [False, False]
        else:
            self.hands = [True, False]
        self.out = True

#-----functions-----#

def next_player(current_player, player_list):
    if current_player == player_list[-1]:
        return player_list[0]
    else:
        return player_list[player_list.index(current_player) + 1]

def next_hand(current_player, hand):
    if hand == 0:
        return 1 if current_player.hands[1] else 0
    else:
        return 0

def next_player_hand(current_player, player_list, hand):
    if current_player == player_list[-1] and hand == 1:
        return player_list[0].hands[0]
    else:
        return player_list[player_list.index(current_player) + 1].hands[hand]

#-----main-----#
players = [Player(x) for x in range(1, players + 1)]
current_player = players[0]

while len(players) > 1:
    hand = 0
    for i in range(syllables):
        if not current_player.out:
            if current_player.hands[hand]:
                if next_player_hand(current_player, players, hand):
                    current_player.put_out()
                else:
                    current_player.spill()
            else:
                if next_player_hand(current_player, players, hand):
                    current_player.put_out()
                else:
                    current_player.spill()
            hand = next_hand(current_player, hand)
        else:
            current_player = next_player(current_player, players)
    players = [x for x in players if not x.out]

print(players[0].number)
