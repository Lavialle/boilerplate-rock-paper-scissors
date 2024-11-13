# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import deque, Counter
max_proba_guess = []
max_proba = []
def player(prev_play, opponent_history=[]):
    global max_proba_guess
    opponent_history.append(prev_play)
    history_size = 20
    window = deque(maxlen=history_size)
    window.append(prev_play)
    counts = Counter(window)
    total = len(window)
    proba = {'R':counts['R'] / total if total > 0 else 0,'P':counts['P'] / total if total > 0 else 0,'S':counts['S'] / total if total > 0 else 0}
    max_proba_guess.append(max(proba, key = proba.get))
    max_proba.append (max(proba))
    first_guess = counter(max_proba_guess[-1])
    verif_cycle, cycle = detect_cycle_pattern(max_proba_guess)
    if verif_cycle == True:
        guess = counter(first_guess[-1])
    else:
        guess = first_guess
    return guess

def counter(guess):
    if guess == 'R':
        return 'P'
    elif guess == 'P':
        return 'S'
    else:
        return 'R'
    
def detect_cycle_pattern(lst):
    n = len(lst)
    for cycle_len in range(1, n // 2 + 1):  
        if n % cycle_len == 0:              
            cycle = lst[:cycle_len]         
            if cycle * (n // cycle_len) == lst:
                return True, cycle          
    return False, []  