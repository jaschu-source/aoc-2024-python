#original template copied for easier use from https://realpython.com/python-advent-of-code/#solving-advent-of-code-with-python f
#adjusted for personal use

from dotenv import load_dotenv
import os
from aocd import get_data

def parse(puzzle_input):
    """Parse input."""

def part1(data):
    """Solve part 1."""

def part2(data):
    """Solve part 2."""

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

# Load .env file from the parent directory
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# # Ensure AOC_SESSION is set correctly
# session = os.getenv("AOC_SESSION")
# print(session)
puzzle_input = get_data(day=1, year=2024)
print(puzzle_input)
solutions = solve(puzzle_input)
print("\n".join(str(solution) for solution in solutions))