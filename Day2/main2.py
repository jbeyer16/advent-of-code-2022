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
}

goal = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
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

cycle = ["rock", "scissors", "paper"]


def main(source):
    if source == "input":
        raw_lines = read_input()
    else:
        raw_lines = read_sample()

    rounds = [line.strip() for line in raw_lines]

    score = 0
    for round in rounds:
        op, go = round.split()

        op = lookup[op]
        go = goal[go]

        if go == "draw":
            me = op
        elif go == "win":
            if op == "rock":
                me = "paper"
                pass
            if op == "paper":
                me = "scissors"
                pass
            if op == "scissors":
                me = "rock"
                pass
        elif go == "lose":
            if op == "rock":
                me = "scissors"
                pass
            if op == "paper":
                me = "rock"
                pass
            if op == "scissors":
                me = "paper"
                pass

        score += outcomes[go]
        score += scores[me]

    print(f"Total score ({source}) is {score}")


if __name__ == "__main__":
    main("sample")
    main("input")
