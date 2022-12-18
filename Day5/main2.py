from collections import deque


def read_sample():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day5/sample.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def read_input():
    with open("/Users/JBEYER/Desktop/AdventOfCode/Day5/input.txt", "r") as fobj:
        lines = fobj.readlines()

    return lines


def parse_stack_line(line):

    clean_line = line.strip("\n")
    stack = []
    num_chars = len(clean_line)

    num_groups = num_chars // 3

    for i in range(num_groups):
        start_ind = 3 * i + i * 1
        end_ind = 3 * i + 3 + i * 1
        stack.append(clean_line[start_ind:end_ind])

    return stack


def main(source):
    if source == "input":
        raw_lines = read_input()
    else:
        raw_lines = read_sample()

    init = []
    instructions = []
    add_to_init = True
    for line in raw_lines:
        if line == "\n":
            add_to_init = False
            continue

        if add_to_init:
            init.append(line)
        else:
            instructions.append(line)

    init.reverse()

    iterable = init.__iter__()

    # stacks = {stack: deque() for stack in next(iterable).split()}
    stacks = []

    while True:
        try:
            line = next(iterable)
            for i, stack in enumerate(parse_stack_line(line)):
                if stack.strip() == "":
                    continue
                try:
                    stacks[i].appendleft(stack.strip())
                except IndexError:
                    stacks.append(deque())
                    stacks[i].appendleft(stack.strip())

        except StopIteration:
            break

    S = {}
    for stack in stacks:
        S[stack.pop()] = stack

    print(S)
    for instruction in instructions:
        print(instruction)
        num = int(instruction.split()[1])
        frm = instruction.split()[3]
        to = instruction.split()[5]

        to_add = []
        for i in range(num):
            item = S[frm].popleft()
            to_add.append(item)

        to_add.reverse()
        for item in to_add:
            S[to].appendleft(item)
        print(S)

    tops = [item[0].replace("[", "").replace("]", "") for item in S.values()]

    result = "".join(tops)

    return result


if __name__ == "__main__":
    result = main("sample")

    print(f"Sample {result=}")
    assert result == "MCD", "Sample did not work"

    result = main("input")
    print(f"Input {result=}")
