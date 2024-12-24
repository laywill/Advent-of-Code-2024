### AI Generated Content ###

import pathlib
from typing import List, Set, Tuple
from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    UP = (0, -1)
    RIGHT = (1, 0)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    
    def turn_right(self) -> 'Direction':
        return {
            Direction.UP: Direction.RIGHT,
            Direction.RIGHT: Direction.DOWN,
            Direction.DOWN: Direction.LEFT,
            Direction.LEFT: Direction.UP
        }[self]

@dataclass
class Guard:
    x: int
    y: int
    facing: Direction
    
    def move(self) -> None:
        dx, dy = self.facing.value
        self.x += dx
        self.y += dy
    
    def get_position(self) -> Tuple[int, int]:
        return (self.x, self.y)
    
    def get_position_in_front(self) -> Tuple[int, int]:
        dx, dy = self.facing.value
        return (self.x + dx, self.y + dy)

class Lab:
    def __init__(self, grid: List[str]):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        
        # Find guard's starting position and direction
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == '^':
                    self.guard = Guard(x, y, Direction.UP)
                    break
                elif grid[y][x] == '>':
                    self.guard = Guard(x, y, Direction.RIGHT)
                    break
                elif grid[y][x] == 'v':
                    self.guard = Guard(x, y, Direction.DOWN)
                    break
                elif grid[y][x] == '<':
                    self.guard = Guard(x, y, Direction.LEFT)
                    break
    
    def is_obstacle(self, x: int, y: int) -> bool:
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        return self.grid[y][x] == '#'
    
    def is_out_of_bounds(self, x: int, y: int) -> bool:
        return not (0 <= x < self.width and 0 <= y < self.height)
    
    def simulate_patrol(self) -> Set[Tuple[int, int]]:
        visited = {self.guard.get_position()}
        
        while True:
            # Check position in front
            front_x, front_y = self.guard.get_position_in_front()
            
            # If out of bounds or obstacle, turn right
            if self.is_obstacle(front_x, front_y):
                self.guard.facing = self.guard.facing.turn_right()
            else:
                # Move forward
                self.guard.move()
                pos = self.guard.get_position()
                
                # If guard left the mapped area
                if self.is_out_of_bounds(*pos):
                    break
                    
                visited.add(pos)
                
        return visited

def read_input(day_number: int) -> List[str]:
    """Read input from a text file."""
    current_dir = pathlib.Path(__file__).parent.parent
    input_path = current_dir / 'inputs' / f'day{day_number:02d}.txt'
    
    with open(input_path, 'r') as f:
        return [line.strip() for line in f.readlines()]

def solve_part1(input_data: List[str]) -> int:
    """
    Solve Part 1: Count distinct positions the guard will visit.
    
    Args:
        input_data: List of strings representing the lab layout
        
    Returns:
        Number of distinct positions visited by the guard
    """
    lab = Lab(input_data)
    visited_positions = lab.simulate_patrol()
    return len(visited_positions)

def solve_part2(input_data: List[str]) -> int:
    """
    Solve Part 2 of the puzzle.
    
    Args:
        input_data: List of strings representing the lab layout
        
    Returns:
        Result of Part 2 solution
    """
    # Implement Part 2 solution here when available
    pass

def main():
    # Automatically extract day number from filename
    day_number = int(pathlib.Path(__file__).stem[3:])
    
    # Read input
    input_data = read_input(day_number)
    
    # Solve Part 1
    part1_solution = solve_part1(input_data)
    print(f"Day {day_number} - Part 1 Solution: {part1_solution}")
    
    # Solve Part 2
    part2_solution = solve_part2(input_data)
    print(f"Day {day_number} - Part 2 Solution: {part2_solution}")

if __name__ == '__main__':
    main()