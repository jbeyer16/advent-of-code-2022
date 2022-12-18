def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day3/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day3/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


PRIORITIES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main(source):
    if source == "input":
        raw_lines = read_input()
    else:
        raw_lines = read_sample()

    rucksacks = [line.strip() for line in raw_lines]

    groups = []
    count = 0
    group = []
    for rucksack in rucksacks:
        group += [rucksack]
        count += 1
        if count == 3:
            groups.append(group)
            group = []
            count = 0

    result = 0
    for group in groups:
        for item in group[0]:
            if item not in group[1] or item not in group[2]:
                continue
            else:
                break
        # print(f"Item is {item=}")
        p = PRIORITIES.index(item) + 1
        result += p

    return result


if __name__ == "__main__":
    result = main("sample")

    print(f"Sample {result=}")
    assert result == 70, "Sample did not work"

    result = main("input")
    print(f"Input {result=}")
