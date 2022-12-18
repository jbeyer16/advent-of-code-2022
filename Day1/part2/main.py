def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day1/part1/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day1/part1/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def main():
    # raw_lines = read_input()
    raw_lines = read_sample()

    lines = [line.strip() for line in raw_lines] + [""]

    sum_ = 0
    most = 0
    largest = []

    for line in lines:
        if line != "":
            sum_ += int(line)
        else:
            most = max(most, sum_)
            largest.append(sum_)
            largest = sorted(largest)[-3:]
            sum_ = 0

        print(line, sum_, largest)
    print(f"Sum is {sum(largest)}")


if __name__ == "__main__":
    main()
