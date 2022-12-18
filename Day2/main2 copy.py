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

goals = {
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


def get_options(choice):
    index = cycle.index(choice)

    options = {}
    try:
        options["winner"] = cycle[index + 1]
    except IndexError:
        options["winner"] = cycle[0]

    options["loser"] = cycle[index - 1]

    return options


def main(source):
    if source == "input":
        raw_lines = read_input()
    else:
        raw_lines = read_sample()

    rounds = [line.strip() for line in raw_lines]

    score = 0
    for round in rounds:
        op, goal = round.split()

        op = lookup[op]
        goal = goals[goal]

        options = get_options(op)

        if goal == "draw":
            # draw
            me = op
        elif goal == "win":
            # i lose
            me = options["loser"]
        elif goal == "lose":
            # i win
            me = options["winner"]

        score += outcomes[goal]
        score += scores[me]

    print(f"Total score ({source}) is {score}")


if __name__ == "__main__":
    main("sample")
    main("input")
