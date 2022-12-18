def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day4/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day4/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def main(source):
    if source == "input":
        raw_lines = read_input()
    else:
        raw_lines = read_sample()

    pairs = [line.strip() for line in raw_lines]

    result = 0

    for pair in pairs:
        p1, p2 = pair.split(",")

        p1_s, p1_e = p1.split("-")
        p2_s, p2_e = p2.split("-")

        p1_s = int(p1_s)
        p1_e = int(p1_e)
        p2_s = int(p2_s)
        p2_e = int(p2_e)

        if (p1_s <= p2_s and p1_e >= p2_s) or (p1_s <= p2_e and p1_e >= p2_e):
            result += 1
            print(f"p1 contains some p2, {p1=} {p2=}")
        elif (p2_s <= p1_s and p2_e >= p1_s) or (p2_s <= p1_e and p2_e >= p1_e):
            result += 1
            print(f"p2 contains p1, {p1=} {p2=}")
        else:
            continue

    return result


if __name__ == "__main__":
    result = main("sample")

    print(f"Sample {result=}")
    assert result == 4, "Sample did not work"

    result = main("input")
    print(f"Input {result=}")
