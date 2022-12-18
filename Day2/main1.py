def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day2/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day2/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


lookup = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

scores = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}

outcomes = {
    "win": 6,
    "lose": 0,
    "draw": 3,
}


def main():
    raw_lines = read_input()
    # raw_lines = read_sample()

    rounds = [line.strip() for line in raw_lines]

    score = 0
    for round in rounds:
        op, me = round.split()

        op = lookup[op]
        me = lookup[me]
        if op == me:
            # tie
            outcome = "draw"
            pass
        elif op == "rock" and me == "paper":
            # me win
            outcome = "win"
            pass
        elif op == "rock" and me == "scissors":
            # op win
            outcome = "lose"
            pass
        elif op == "paper" and me == "rock":
            # op win
            outcome = "lose"
            pass
        elif op == "paper" and me == "scissors":
            outcome = "win"
            # me win
            pass
        elif op == "scissors" and me == "rock":
            outcome = "win"
            # me win
            pass
        elif op == "scissors" and me == "paper":
            # op win
            outcome = "lose"
            pass

        score += outcomes[outcome]
        score += scores[me]

    print(f"Total score is {score}")


if __name__ == "__main__":
    main()
