

#-----main-----
syllables, players = [int(x) for x in input().split()]

#-----classes-----
class Player:
    def __init__(self, number):
        self.number = number
        self.hands = [0, 0]
        self.out = False

    def crack(self):
        self.hands = [1, 1]

    def spill(self):
        for i in range(2):
            if self.hands[i]:
                self.hands[i] = 0
                break

    def put_out(self):
        if self.hands[0] == 0 and self.hands[1] == 0:
            self.hands[0] = 1
            self.hands[1] = 1
        else:
            self.hands[0] = 0
            self.hands[1] = 0
        self.out = True

#-----functions-----
def next_player(current_player, players):
    if current_player == players[-1]:
        return players[0]
    else:
        return players[players.index(current_player) + 1]

def next_hand(current_player):
    if current_player.hands[0]:
        return 1
    else:
        return 0

def next_player_hand(current_player, players, hand):
    if current_player.number == players[-1].number and hand == 1:
        return players[0].hands[0] == 0
    else:
        return players[players.index(current_player) + 1].hands[hand] == 0

#-----main-----
players = [Player(x) for x in range(1, players + 1)]
current_player = players[0]

while len(players) > 1:
    for i in range(syllables):
        if not current_player.out:
            if current_player.hands[0] == 1 and current_player.hands[1] == 1:
                current_player.crack()
            elif current_player.hands[0] == 0 and current_player.hands[1] == 0:
                if next_player_hand(current_player, players, next_hand(current_player)):
                    current_player.put_out()
                else:
                    current_player.spill()
            elif current_player.hands[0] == 1 or current_player.hands[1] == 1:
                if next_player_hand(current_player, players, next_hand(current_player)):
                    current_player.put_out()
                else:
                    current_player.spill()
        current_player = next_player(current_player, players)
    players = [x for x in players if not x.out]

print(players[0].number)
