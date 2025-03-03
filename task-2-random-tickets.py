import random

def get_numbers_ticket(min, max, quantity):
    win_sequences = list()
    if min < 0 or max > 1000:
        return win_sequences
    else:
        while len(win_sequences) < quantity:
            win_sequences.append(random.randrange(min, max))
            win_sequences = sorted(set(win_sequences))
            win_sequences = list(win_sequences)
    return win_sequences 


