from dotenv import load_dotenv
import os
from aocd import get_data

def parse(puzzle_input):
    parsed_puzzle = []
    for line in puzzle_input.split("\n"):
        parsed_puzzle.append(line.split())

    return parsed_puzzle

def part1(data):
    result = 0
    for line in data:
        line_save = True
        increasing = False
        for index, value in enumerate(line):
            line_lenght = len(line) - 1
            if index < line_lenght:
                next_value = int(line[index + 1])
            if index == 0:
                increasing = int(value) < next_value
            if increasing and (index < line_lenght):
                line_save = (int(value) < next_value) and (next_value - int(value) > 0) and (next_value - int(value) <= 3)
            elif (not increasing) and (index < line_lenght):
                line_save = (int(value) > next_value) and (int(value) - next_value > 0) and (int(value) - next_value <= 3)
            if not line_save:
                break
            if index == line_lenght:
                result = result + 1
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

puzzle_input = get_data(day=2, year=2024)
solutions = solve(puzzle_input)
print("\n".join(str(solution) for solution in solutions))