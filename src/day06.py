### AI Generated Content ###

import pathlib
import logging
import time
from typing import List, Set, Tuple
from dataclasses import dataclass
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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
    
    def __str__(self):
        return self.name

@dataclass
class Guard:
    x: int
    y: int
    facing: Direction
    
    def move(self) -> None:
        dx, dy = self.facing.value
        self.x += dx
        self.y += dy
        logger.debug(f"Guard moved to position ({self.x}, {self.y}) facing {self.facing}")
    
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
        self.start_time = None
        self.timeout_seconds = 5  # Set timeout to 5 seconds
        
        # Find guard's starting position and direction
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == '^':
                    self.guard = Guard(x, y, Direction.UP)
                    logger.info(f"Guard initialized at ({x}, {y}) facing UP")
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
            logger.debug(f"Position ({x}, {y}) is out of bounds")
            return True
        is_obstacle = self.grid[y][x] == '#'
        if is_obstacle:
            logger.debug(f"Found obstacle at ({x}, {y})")
        return is_obstacle
    
    def is_out_of_bounds(self, x: int, y: int) -> bool:
        result = not (0 <= x < self.width and 0 <= y < self.height)
        if result:
            logger.debug(f"Position ({x}, {y}) is out of bounds")
        return result
    
    def check_timeout(self):
        if self.start_time is None:
            self.start_time = time.time()
        elif time.time() - self.start_time > self.timeout_seconds:
            logger.error(f"Simulation timed out after {self.timeout_seconds} seconds")
            raise TimeoutError(f"Simulation timed out after {self.timeout_seconds} seconds")
    
    def simulate_patrol(self) -> Set[Tuple[int, int]]:
        self.start_time = time.time()
        visited = {self.guard.get_position()}
        steps = 0
        
        while not self.is_out_of_bounds(self.guard.x, self.guard.y):
            self.check_timeout()
            steps += 1
            logger.debug(f"Step {steps}: Guard at {self.guard.get_position()} facing {self.guard.facing}")
            
            # Check position in front
            front_x, front_y = self.guard.get_position_in_front()
            logger.debug(f"Checking position in front: ({front_x}, {front_y})")
            
            # If out of bounds or obstacle, turn right
            if self.is_obstacle(front_x, front_y):
                logger.debug(f"Obstacle detected, turning right from {self.guard.facing}")
                self.guard.facing = self.guard.facing.turn_right()
                logger.debug(f"New direction: {self.guard.facing}")
            else:
                # Move forward
                self.guard.move()
                pos = self.guard.get_position()
                visited.add(pos)
                logger.debug(f"Added position {pos} to visited set. Total visited: {len(visited)}")
        
        logger.info(f"Patrol completed. Visited {len(visited)} distinct positions in {steps} steps")
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
    # Configure logging for main execution
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
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