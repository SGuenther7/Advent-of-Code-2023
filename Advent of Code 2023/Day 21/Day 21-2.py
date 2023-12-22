#testData = [
#    "...........",
#    ".....###.#.",
#    ".###.##..#.",
#    "..#.#...#..",
#    "....#.#....",
#    ".##..S####.",
#    ".##..#...#.",
#    ".......##..",
#    ".##.#.####.",
#    ".##..##.##.",
#    "...........",
#]
#
#import heapq
#def findWay2(grid, start, maxSteps):
#    Q = [(0, start[1], start[0])]
#    D = {}
#    R = len(grid)
#    C = len(grid[0])
#
#    col = list(grid[start[1]])
#    print(f"START: {start}") 
#
#    while Q:
#        dist,r,c = heapq.heappop(Q)
#        if (r,c) in D:
#            #assert dist >= D[(r,c,dir_,indir)]
#            continue
#        D[(r,c)] = dist
#        for i,(dr,dc) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
#            rr = r+dr
#            cc = c+dc
#
#            if 0<=rr<R and 0<=cc<C :
#                if grid[rr][cc] == "#":
#                    continue
#                
#                cost = 1
#                heapq.heappush(Q, (dist+cost, rr, cc))
#
#    ans = 0
#    #print(D)
#    i = 0
#    for (r,c),v in D.items():
#        #if grid[r][c] != "#" and v <= maxSteps:
#        #    col = list(grid[r]) 
#        #    col[c] = "_"
#        #    grid[r] = "".join(col)
#        #    i += 1
#
#        if (maxSteps - v) % 2 == 0 and v <= maxSteps:
#            #print(((r, c),v))
#            
#        #    col = list(grid[r]) 
#        #    col[c] = "0"
#        #    grid[r] = "".join(col)
#
#            ans += 1 
#
#    #for line in grid:
#    #    print(line)
##
#    #print(f"{i} of {len(D)}")
#    return ans
#
#from math import floor
#from collections import deque
#
#import os
#os.system('cls' if os.name == 'nt' else 'clear')
#
#def makeLarger(data, grid_width):
#    largerGrid = []
#    for grid in range(grid_width):
#        print(grid)
#        for i in range(len(data[0])):
#            largerGrid.append("".join([data[i] for _ in range(grid_width)]))
#
#    return largerGrid
#
#def findWay(grid, start, maxSteps):
#    sc, sr = start
#
#    ans = set()
#    seen = {(sr, sc)}
#    q = deque([(sr, sc, maxSteps)])
#
#    while q:
#        r, c, s = q.popleft()
#
#        if s % 2 == 0:
#            ans.add((r,c))
#        if s == 0:
#            continue
#
#        for nr, nc in [(r + 1, c), (r -1, c), (r, c + 1), (r, c - 1)]:
#            if  nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
#                continue
#            seen.add((nr, nc))
#            q.append((nr, nc, maxSteps - 1))
#    
#    return len(ans)
#
#def doIt(data : [str]) -> int:
#    
#    for i in range(len(data)):
#        data[i] = data[i].strip()    
#
#    start = (-1,-1)
#
#    for row in range(len(data)):
#        for col in range(len(data[row])):
#            if data[row][col] == "S":
#                start = (row, col)
#    
#    size = len(data)
#    maxSteps = 6
#    
#    print(f"{start} {size // 2} {size / 2}")
#    assert start[0] == start[1] == size // 2
#    assert len(data) == len(data[0])
#    
#    maxSteps = 10
#    #maxSteps = 50
#    #maxSteps = 100
#    #maxSteps = 500
#    #maxSteps = 1000
#    #maxSteps = 5000
#    maxSteps = 26501365
#
##    print(f"{maxSteps % size} {size // 2} {size}")
##    assert maxSteps % size == size // 2
##
#    grid_width = maxSteps // size -1
#    print(f"grid_width: {grid_width}")
#    print(f"size: {size}")
#
#    #largeGrid = makeLarger(data, grid_width)
#
#    odd  = (grid_width // 2 * 5 + 1) ** 2
#    even = (grid_width // 2 * 5 ) ** 2
#
#    print("odd even")
#    odd_points  = findWay(data, start, size * 4 + 1)
#    even_points = findWay(data, start, size * 4)
#    
#    print("corner")
#    cornerTop    = findWay(data, (start[0], 0),        size - 1)
#    cornerBottom = findWay(data, (start[0], size - 1), size - 1)
#    cornerLeft   = findWay(data, (0, start[1]),        size - 1)
#    cornerRight  = findWay(data, (size - 1, start[1]), size - 1)
#
#    print("small")
#    small_TR = findWay(data, (0, size - 1),        size // 2 - 1)
#    small_BR = findWay(data, (0, 0),               size // 2 - 1)
#    small_TL = findWay(data, (size - 1, size - 1), size // 2 - 1)
#    small_BL = findWay(data, (size - 1, 0),        size // 2 - 1)
#
#    print("big")
#    big_TR = findWay(data, (0, size - 1),        size * 3 // 2 - 1)
#    big_BR = findWay(data, (0, 0),               size * 3 // 2 - 1)
#    big_TL = findWay(data, (size - 1, size - 1), size * 3 // 2 - 1)
#    big_BL = findWay(data, (size - 1, 0),        size * 3 // 2 - 1)
#
#    #mid = len(largeGrid) //2
#    #way = findWay(largeGrid, (mid, mid), maxSteps)
#    #way = findWay(data, start, 64)
#
#    #ans = way
#
##    print("-------\n")
##    print(
##        odd * odd_points + even * even_points 
##        + cornerBottom + cornerTop + cornerRight + cornerLeft 
##        + (grid_width + 1) * (small_BL + small_BR + small_TL + small_TR) 
##        + grid_width * (big_BL + big_BR + big_TL + big_TR) 
##        )
#
#    ans = odd * odd_points + even * even_points \
#        + cornerBottom + cornerTop + cornerRight + cornerLeft \
#        + (grid_width + 1) * (small_BL + small_BR + small_TL + small_TR) \
#        + grid_width * (big_BL + big_BR + big_TL + big_TR) 
#
#    
#    #print(f"----------\n{findWay(data, start, 6)}\n----------")
##    for line in data:
##        print(line)
#
#    return ans    
#
#from time import process_time, sleep
#import datetime
#
#def main():
#
#    file = open("..\Python\Advent of Code 2023\Day 21\input.txt", 'r')
#
#    data = file.readlines() 
#    #data = testData
#
#    print(datetime.datetime.now())    
#
#    answer = doIt(data)
#
#    print("-------\n")
#    print(answer)
#    print("\n-------")
#
#    # Part 1
#    # 3_594 First Try :)
#    # Part 2
#    # 605_241_159_858_707 Too low
#    # 605241159858707
#    # 605241154598946
#    # 605241159858707
#    # 3782714421185570
#    # 3782727841443285
#    t = process_time()
#    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")
#
#if __name__ == "__main__":
#    main()
#

# https://github.com/WinslowJosiah/adventofcode/blob/main/aoc2023/day21/__init__.py
from collections import deque
from collections.abc import Iterable
from itertools import starmap
from operator import add

type Vector = tuple[int, ...]

def count_paths(
        src_node: Vector,
        path_length: int,
        grid: list[str],
) -> int:
    """
    Count the number of paths with a length of `path_length` from
    `src_node` in a grid of tiles. The paths are allowed to double back
    on themselves.
    """
    result = 0

    height = len(grid)
    width = len(grid[0])

    visited: set[Vector] = set()
    # This is basically a standard breadth-first search
    queue: deque[tuple[int, Vector]] = deque([(0, src_node)])
    while queue:
        cost, node = queue.popleft()

        # If node has been visited before
        if node in visited:
            # Don't explore this path any further
            continue
        visited.add(node)

        # If the current path's parity is the same as the parity of the
        # specified path length
        if cost % 2 == path_length % 2:
            # This path can be reached in the specified number of steps
            result += 1
            # NOTE: We can do this because all paths between any two
            # tiles will have the same parity.
        # If path becomes longer than specified path length
        if cost >= path_length:
            # Don't explore this path any further
            continue

        for offset in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            # Get coordinates at offset
            next_row, next_col = starmap(add, zip(node, offset))
            # If this plot of land is not empty
            if grid[next_row % height][next_col % width] == "#":
                # This neighbor is not valid
                continue
            # Append this neighbor to the queue
            queue.append((cost + 1, (next_row, next_col)))

    return result


def aoc2023_day21_part1(lines: Iterable[str]) -> int:
    grid = list(lines)
    height = len(grid)
    width = len(grid[0])
    # The elf starts in the center of the grid
    return count_paths((height // 2, width // 2), 64, grid)


def aoc2023_day21_part2(lines: Iterable[str]) -> int:
    steps_to_take = 26501365

    grid = list(lines)
    height = len(grid)
    width = len(grid[0])
    # XXX: I hate how simple this looks. I hate how complicated the
    # problem was. I hate how many assumptions I needed to make about
    # the input data to even start arriving at a formula for the answer.
    # I hate how these assumptions were not a part of the specifications
    # or the example data. I hate how the formula I arrived at didn't
    # work. I hate how even other people's formulas didn't work for my
    # input. I hate how I know after all of this that the answer is the
    # result of some quadratic equation that I couldn't derive myself
    # and that I don't even know the coefficients of. I hate, hate,
    # hate, hate, hate, hate, hate this problem. Get it out of my sight.

    n = steps_to_take // width
    # The elf starts in the center of the grid
    a, b, c = (
        count_paths((height // 2, width // 2), s * width + (width // 2), grid)
        for s in range(3)
    )
    # NOTE: This part of my solution comes verbatim from someone else.
    # (No, I won't explain it. No, I'm not sorry.)
    return a + n * (b - a + (n - 1) * (c - b - b + a) // 2)

parts = (aoc2023_day21_part1, aoc2023_day21_part2)

def doIt(data : [str]) -> int:
    
    for i in range(len(data)):
        data[i] = data[i].strip()    

    for line in data:
        print(line)

    ans = aoc2023_day21_part2(data)

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 21\input.txt", 'r')

    data = file.readlines() 

    print(datetime.datetime.now())    

    answer = doIt(data)
    print("\n-------")
    print(answer)
    print("\n-------")
       

    # Part 1
    # 3_594 First Try :)
    # Part 2
    # 605_241_159_858_707 Too low
    # 605241159858707
    # 605241154598946
    # 605241159858707
    # 3782714421185570
    # 3782727841443285

    # 605247138198755 bullshit
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()
