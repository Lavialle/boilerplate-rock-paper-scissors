# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_opponent_play, opponent_history=[], my_history=[], num_games=[0], cycle=[None], detected_bot=[None], window_size=100):
    
    # Append the opponent's previous play to history, keep only the last 'window_size' plays
    num_games[0] += 1 # Increment game count
    if prev_opponent_play:
        opponent_history.append(prev_opponent_play)
        if len(opponent_history) > window_size:
            opponent_history.pop(0)
    # Player last play
    if len(my_history) == 0:
        last_my_play = "R"
    else:
        last_my_play = my_history[-1]   


    # Detect cycle pattern
    def detect_cycle_pattern(lst):
        n = len(lst)
        for cycle_len in range(1, n // 2 + 1):
            if n % cycle_len == 0:
                pattern = lst[:cycle_len]
                if pattern * (n // cycle_len) == lst:
                    return pattern
        return None

    # Bot detection functions
    def is_quincy():
        pattern = ["R", "R", "P", "P", "S"]
        if cycle[0] is None or len(cycle[0]) != 5:
            return False
        for i in range(5):
            if cycle[0] == pattern[i:] + pattern[:i]:
                return True
        return False

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

        if len(my_history) < 30:  # avoid noise
            return False

        match, total = 0, 0
        play_order = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }

        # Analyze only the last 'window_size' plays
        start = max(1, len(my_history) - window_size)

        for i in range(start, len(my_history)):
            prev = my_history[i-1]
            curr = my_history[i]

            # Update play order
            pair = prev + curr
            if pair in play_order:
                play_order[pair] += 1

            # Predicion based on previous play
            potential_plays = [prev + "R", prev + "P", prev + "S"]
            sub_order = {k: play_order[k] for k in potential_plays}
            prediction = max(sub_order, key=sub_order.get)[-1]

            if i < len(opponent_history):
                expected = counter(prediction)
                if opponent_history[i] == expected:
                    match += 1
                total += 1

        if total == 0:
            return False
        return match / total >= 0.55


    # Define strategies
    def counter_quincy():
        return counter(cycle[0][num_games[0]%len(cycle[0])])

    def counter_abbey():
        if len(my_history) < 2:
            return random.choice(["R", "P", "S"])
            # Some randomness to break symmetry
        if random.random() < 0.1:
            return random.choice(["R", "P", "S"])
        prev = my_history[-1]
        transitions = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
        for i in range(1, len(my_history)):
            pair = my_history[i-1] + my_history[i]
            if pair in transitions:
                transitions[pair] += 1

        potential = [prev + "R", prev + "P", prev + "S"]
        sub_order = {k: transitions[k] for k in potential}
        prediction = max(sub_order, key=sub_order.get)[-1]

        return counter(counter(prediction))

    def counter_mrugesh():
        last_ten = my_history[-10:]
        most_freq = max(set(last_ten), key=last_ten.count)
        guess = counter(most_freq)
        return counter(guess)

    def counter_kris():
        return counter(counter(last_my_play))

    if (len(opponent_history) == 50 and detected_bot[0] is None) or (num_games[0] % 10 == 0 and len(opponent_history) > 0):
        cycle[0] = detect_cycle_pattern(opponent_history)
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
        # print(f"Detected bot: {detected_bot[0]}")


    # move choice based on the detected bot
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

    my_history.append(move)
    if len(my_history) > window_size:
        my_history.pop(0)
    return move

# Counter function instead of a dictionary
def counter(guess):
    if guess == 'R':
        return 'P'
    elif guess == 'P':
        return 'S'
    else:
        return 'R'

