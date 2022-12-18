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

    result = 0

    for rucksack in rucksacks:
        c1 = rucksack[: len(rucksack) // 2]
        c2 = rucksack[len(rucksack) // 2 :]

        for item in c1:
            if item in c2:
                break
        else:
            raise Exception("could not find item")

        p = PRIORITIES.index(item) + 1
        # print(rucksack, item, p)
        result += p
    return result


if __name__ == "__main__":
    result = main("sample")

    print(f"Sample {result=}")
    assert result == 157, "Sample did not work"

    result = main("input")
    print(f"Input {result=}")
