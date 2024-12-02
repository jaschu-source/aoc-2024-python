from dotenv import load_dotenv
import os
from aocd import get_data

def parse(puzzle_input):
    puzzle = []
    puzzle_left = []
    puzzle_right = []

    for line in puzzle_input.split("\n"):
        split_line = line.split()
        puzzle_left.append(split_line[0])
        puzzle_right.append(split_line[1])
    
    puzzle.append(puzzle_left)
    puzzle.append(puzzle_right)

    return puzzle

def part1(data):
    result = 0
    data[0].sort()
    data[1].sort()
    for index, value in enumerate(data[0]):
        if data[0][index] >= data[1][index]:
            result = result + (int(data[0][index]) - int(data[1][index]))
        else:
            result = result + (int(data[1][index]) - int(data[0][index]))
    return result

def part2(data):
    result = 0
    for right_number in data[0]:
        count = 0
        for left_number in data[1]:
            if right_number == left_number:
                count = count + 1
        result = result + int(right_number) * count
    return result

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# Load .env file from the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

puzzle_input = get_data(day=1, year=2024)
solutions = solve(puzzle_input)
print("\n".join(str(solution) for solution in solutions))