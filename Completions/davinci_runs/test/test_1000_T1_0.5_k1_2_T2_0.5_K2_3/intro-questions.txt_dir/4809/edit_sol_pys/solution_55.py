
# -----main-----
syllables, players = [int(x) for x in input().split()]

# -----classes-----
class Player:
    def __init__(self, number):
        self.number = number
        self.hands = [True, True]
        self.out = False

    def crack(self):
        self.hands = [False, False]

    def spill(self):
        for i in range(2):
            if self.hands[i]:
                self.hands[i] = True
                break

    def put_out(self):
        if not self.hands[0] and not self.hands[1]:
            self.hands[0] = False
            self.hands[1] = False
        else:
            self.hands[0] = True
            self.hands[1] = True
        self.out = True

# -----functions-----
def next_player(current_player, players):
    if current_player == players[-1].number:
        return players[0]
    else:
        return players[players.index(current_player) + 1].number

def next_hand(current_player):
    if current_player.hands[0]:
        return 1
    else:
        return 0

def next_player_hand(current_player, players, hand):
    if current_player.number == players[-1].number and hand == 1:
        return players[0].hands[0]
    else:
        return players[players.index(current_player) + 1].hands[hand]  

# -----main-----
players = [Player(x) for x in range(1, players + 1)]
current_player = players[0].number

while len(players) > 1:
    for i in range(syllables):
        if not players[current_player - 1].out:
            if not players[current_player - 1].hands[0] and not players[current_player - 1].hands[1]:
                players[current_player - 1].crack()
            elif players[current_player - 1].hands[0] and players[current_player - 1].hands[1]:
                if next_player_hand(players[current_player - 1], players, next_hand(players[current_player - 1])):
                    players[current_player - 1].put_out()
                else:
                    players[current_player - 1].spill()
            elif not players[current_player - 1].hands[0] or not players[current_player - 1].hands[1]:
                if next_player_hand(players[current_player - 1], players, next_hand(players[current_player - 1])):
                    players[current_player - 1].put_out()
                else:
                    current_player.spill()
        current_player = next_player(current_player, players)
    players = [x for x in players if not x.out]

print(players[0].number)
