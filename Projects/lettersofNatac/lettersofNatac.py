from collections import Counter
def play_if_enough(hand, play):
    # count the elements in hand
    if hand != '':
        counter_hand = Counter(hand)
        counter_play = Counter(play)
        # Determine valid play
        for key, value in counter_play.items():
            if counter_hand[key] > value:
                build = True
                # subtract current play from hand
                counter_hand[key] = counter_hand[key] - value
            else:
                build = False
        # rebuild hand
        return_list = ''
        if build:
            for key, value in counter_hand.items():
                return_list = return_list + (key * value)
            return (True, return_list)
        else:
            return (False, hand)
    else:
        return (False, hand)



print(play_if_enough("ooooogggssbbb", "ooogg"))
print(play_if_enough("oogssbbb", "bwsg"))
print(play_if_enough("", "bw"))
print(play_if_enough("abcdefghij", "aa"))