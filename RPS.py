# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
from collections import Counter
def player(prev_play, opponent_history=[], max_proba_guess=[], window_size=6):
    # Append the opponent's previous play to history
    if prev_play:
        opponent_history.append(prev_play)
    
    # Define strategies
    def counter_quincy():
        choices = ["P", "P", "S", "S", "R"]
        return choices[len(opponent_history) % len(choices)]

    def counter_abbey():
        pass

    def counter_mrugesh():
        pass

    def counter_kris():
        pass
    
    # Initial exploration phase
    if len(opponent_history) < 10:
        return "R"  # Neutral start
    

    return counter_quincy()

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