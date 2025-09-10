# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
def player(prev_opponent_play, opponent_history=[], my_history=[], cycle=[None], detected_bot = [None]):
    # Append the opponent's previous play to history
    if prev_opponent_play:
        opponent_history.append(prev_opponent_play)
    # Historique du joueur
    if len(my_history) == 0:
        last_my_play = "R"
    else:
        last_my_play = my_history[-1]    

    def detect_cycle_pattern(lst):
        n = len(lst)
        for cycle_len in range(1, n // 2 + 1):
            if n % cycle_len == 0:
                pattern = lst[:cycle_len]
                if pattern * (n // cycle_len) == lst:
                    return pattern
        return None

    def is_quincy():
        return cycle[0] == ["R","P","P","S","R"]

    def is_mrugesh():
        if len(opponent_history) < 11:
            return False
        match = 0
        for i in range(10, len(opponent_history)):
            last_ten = my_history[i-10:i]
            if not last_ten:
                continue
            most_freq = max(set(last_ten), key=last_ten.count)
            if opponent_history[i] == counter(most_freq):
                match += 1
        return match / (len(opponent_history)-10) > 0.8


    def is_kris():
        if len(opponent_history) < 2:
            return False
        match = 0
        for i in range(1, len(opponent_history)):
            if counter(my_history[i-1]) == opponent_history[i]:
                match += 1
        return match / (len(opponent_history)-1) > 0.9

    def is_abbey():
        if len(my_history) < 3:
            return False
        match = 0
        for i in range(2, len(opponent_history)):
            prev_pair = "".join(my_history[i-2:i])
            next_moves = []
            for j in range(2, i):
                if "".join(my_history[j-2:j]) == prev_pair:
                    next_moves.append(my_history[j])
            if next_moves:
                prediction = max(set(next_moves), key=next_moves.count)
                # Abbey joue le coup qui bat cette prédiction
                if opponent_history[i] == counter(prediction):
                    match += 1
        return match / (len(opponent_history)-2) > 0.6

    # Define strategies
    def counter_quincy():
        return counter(cycle[0][len(opponent_history)%len(cycle[0])])

    def counter_abbey():
        if len(my_history) < 2:
            return "R"
        prev_pair = "".join(my_history[-2:])
        # Cherche le coup le plus fréquent après cette paire
        next_moves = []
        for i in range(len(my_history)-2):
            if "".join(my_history[i:i+2]) == prev_pair:
                next_moves.append(my_history[i+2])
        if next_moves:
            prediction = max(set(next_moves), key=next_moves.count)
            # Abbey va jouer le coup qui bat cette prédiction
            # Donc, nous jouons le coup qui bat le coup d'Abbey
            return counter(counter(prediction))
        else:
            return "R"

    def counter_mrugesh():
        last_ten = my_history[-10:]
        most_freq = max(set(last_ten), key=last_ten.count)
        guess = counter(most_freq)
        return counter(guess)

    def counter_kris():
        return counter(counter(last_my_play))

    # Detect cycle pattern if not already detected
    if len(opponent_history) == 10 and  cycle[0] is None:
        cycle[0] = detect_cycle_pattern(opponent_history)

        # Détection unique après 15 coups
    if len(opponent_history) == 15 and detected_bot[0] is None:
        if is_quincy():
            detected_bot[0] = "quincy"
        elif is_kris():
            detected_bot[0] = "kris"
        elif is_mrugesh():
            detected_bot[0] = "mrugesh"
        elif is_abbey():
            detected_bot[0] = "abbey"
        else:
            detected_bot[0] = "unknown"

    # Utilisation du bot détecté
    if detected_bot[0] == "quincy":
        move = counter_quincy()
    elif detected_bot[0] == "mrugesh":
        move = counter_mrugesh()
    elif detected_bot[0] == "kris":
        move = counter_kris()
    elif detected_bot[0] == "abbey":
        move = counter_abbey()
    else:
        move = random.choice(["R", "S", "P"])

    print(f"Detected bot:{detected_bot[0]}")
    my_history.append(move)
    return move


def counter(guess):
    if guess == 'R':
        return 'P'
    elif guess == 'P':
        return 'S'
    else:
        return 'R'

