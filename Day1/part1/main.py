def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day1/part1/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day1/part1/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    raw_lines = read_input()

    lines = [l.strip() for l in raw_lines]

    sum = 0
    most = 0
    for line in lines:
        if line != "":
            sum += int(line)
        else:
            most = max(most, sum)
            sum = 0
        print(line, sum, most)

    print(f"Largest was {most}")


if __name__ == "__main__":
    main()
