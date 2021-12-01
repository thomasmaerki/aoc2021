# Day 1

def main():
    
    with open("input.txt") as f:
        input = [int(line.rstrip()) for line in f.readlines()]

    # Part 1
    count = 0
    for i in range(len(input)-1):
        if input[i+1] > input[i]:
            count += 1
    
    print(f"Solution first part: {count}")

    # Part 2
    count = 0
    for i in range(len(input)-3):
        first_measurement = sum(input[i:i+3])
        second_measurement = sum(input[i+1:i+4])
        if second_measurement > first_measurement:
            count += 1
    
    print(f"Solution second part: {count}")


main()