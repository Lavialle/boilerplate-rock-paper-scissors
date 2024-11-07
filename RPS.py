# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import deque, Counter
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    history_size = 20
    window = deque(maxlen=history_size)
    window.append(prev_play)
    counts = Counter(window)
    total = len(window)
    proba = {'R':counts['R'] / total if total > 0 else 0,'P':counts['P'] / total if total > 0 else 0,'S':counts['S'] / total if total > 0 else 0}
    max_proba = max(proba, key = proba.get)
    if max_proba == 'R':
        guess = 'P'
    elif max_proba == 'P':
        guess = 'S'
    else:
        guess = 'R'
    return guess
