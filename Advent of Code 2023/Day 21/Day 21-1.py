testData = [
    "...........",
    ".....###.#.",
    ".###.##..#.",
    "..#.#...#..",
    "....#.#....",
    ".##..S####.",
    ".##..#...#.",
    ".......##..",
    ".##.#.####.",
    ".##..##.##.",
    "...........",
]

import heapq
def findWay(grid, start):
    Q = [(0, start[1], start[0])]
    D = {}
    R = len(grid)
    C = len(grid[0])

    col = list(grid[start[1]])
    print(start) 

    while Q:
        dist,r,c = heapq.heappop(Q)
        if (r,c) in D:
            #assert dist >= D[(r,c,dir_,indir)]
            continue
        D[(r,c)] = dist
        for i,(dr,dc) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            rr = r+dr
            cc = c+dc

            if 0<=rr<R and 0<=cc<C :
                if grid[rr][cc] == "#":
                    continue
                
                cost = 1
                heapq.heappush(Q, (dist+cost, rr, cc))

    ans = 0
    print(D)
    maxSteps = 64
    i = 0
    for (r,c),v in D.items():
        if grid[r][c] != "#" and v <= maxSteps:
            col = list(grid[r]) 
            col[c] = "_"
            grid[r] = "".join(col)
            i += 1

        if (maxSteps - v) % 2 == 0 and v <= maxSteps:
            print(((r, c),v))
            
            col = list(grid[r]) 
            col[c] = "0"
            grid[r] = "".join(col)

            ans += 1 

    for line in grid:
        print(line)

    print(f"{i} of {len(D)}")
    return ans

from math import floor

def doIt(data : [str]) -> int:
    
    for i in range(len(data)):
        data[i] = data[i].strip()    

    start = (-1,-1)

    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "S":
                start = (row, col)
    
    way = findWay(data, start)

    ans = way

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 21\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 3_594 First Try :)
    # Part 2
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()
