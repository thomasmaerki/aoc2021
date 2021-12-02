# Day 2

def main():
    
    with open("input.txt") as f:
        input = [line.rstrip() for line in f.readlines()]

    # Split direction and units
    input = [x.split() for x in input]

    # Part 1
    position = 0
    depth = 0

    for step in input:
        direction = step[0]
        unit = int(step[1])
        if direction == 'forward':
            position += unit
        elif direction == 'down':
            depth += unit
        elif direction == 'up':
            depth -= unit

    print(f"Solution first part: {depth * position}")

    # Part 2
    position = 0
    depth = 0
    aim = 0

    for step in input:
        direction = step[0]
        unit = int(step[1])
        if direction == 'forward':
            position += unit
            depth += aim * unit
        elif direction == 'down':
            aim += unit
        elif direction == 'up':
            aim -= unit
    
    print(f"Solution second part: {depth * position}")


main()
