

def card_to_value(card):
    return '23456789TJQKA'.index(card[0])

def card_to_suit(card):
    return 'CDHS'.index(card[1])

def is_flush(cards):
    suit = card_to_suit(cards[0])
    for card in cards[1:]:
        if suit != card_to_suit(card):
            return False
    return True

def is_straight(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    if values[0] == 0:
        values.append(14)
    for i in range(1, len(values)):
        if values[i] - values[i-1] != 1:
            return False
    return True

def is_four_of_a_kind(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    if values[0] == values[1] == values[2] == values[3]:
        return True
    if values[1] == values[2] == values[3] == values[4]:
        return True
    return False

def is_three_of_a_kind(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    if values[0] == values[1] == values[2]:
        return True
    if values[1] == values[2] == values[3]:
        return True
    if values[2] == values[3] == values[4]:
        return True
    return False

def is_two_pair(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    if values[0] == values[1] and values[2] == values[3]:
        return True
    if values[0] == values[1] and values[3] == values[4]:
        return True
    if values[1] == values[2] and values[3] == values[4]:
        return True
    return False

def is_pair(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    if values[0] == values[1]:
        return True
    if values[1] == values[2]:
        return True
    if values[2] == values[3]:
        return True
    if values[3] == values[4]:
        return True
    return False

def get_highest_card(cards):
    values = [card_to_value(card) for card in cards]
    values.sort()
    return values[-1]

def get_strength(cards):
    if is_flush(cards) and is_straight(cards):
        return 8
    if is_four_of_a_kind(cards):
        return 7
    if is_flush(cards):
        return 6
    if is_straight(cards):
        return 5
    if is_three_of_a_kind(cards):
        return 4
    if is_two_pair(cards):
        return 3
    if is_pair(cards):
        return 2
    return 1

def get_tiebreaker(cards):
    if is_flush(cards) and is_straight(cards):
        return get_highest_card(cards)
    if is_four_of_a_kind(cards):
        return get_highest_card(cards)
    if is_flush(cards):
        return get_highest_card(cards)
    if is_straight(cards):
        return get_highest_card(cards)
    if is_three_of_a_kind(cards):
        return get_highest_card(cards)
    if is_two_pair(cards):
        values = [card_to_value(card) for card in cards]
        values.sort()
        if values[0] == values[1] and values[2] == values[3]:
            return [values[0], values[2]]
        if values[0] == values[1] and values[3] == values[4]:
            return [values[0], values[3]]
        if values[1] == values[2] and values[3] == values[4]:
            return [values[1], values[3]]
    if is_pair(cards):
        values = [card_to_value(card) for card in cards]
        values.sort()
        if values[0] == values[1]:
            return [values[0]]
        if values[1] == values[2]:
            return [values[1]]
        if values[2] == values[3]:
            return [values[2]]
        if values[3] == values[4]:
            return [values[3]]
    return get_highest_card(cards)

cards = input().split()
print(get_strength(cards), get_tiebreaker(cards))
