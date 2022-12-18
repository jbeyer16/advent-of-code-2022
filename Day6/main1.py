def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day6/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def main(source):
    if source == "input":
        raw_lines = [read_input()[0].strip()]
    else:
        raw_lines = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb"]

    window = []
    for i, ch in enumerate(raw_lines[0], 1):
        window.append(ch)

        if len(window) < 14:
            continue

        window = window[-14:]

        if len(window) == len(set(window)):
            print(f"{window} has unique letters")
            break
        print(ch, window)

    result = i
    return result


if __name__ == "__main__":
    result = main("sample")

    print(f"Sample {result=}")
    assert result == 19, "Sample did not work"

    result = main("input")
    print(f"Input {result=}")
