testData = [
    "2413432311323\n",
    "3215453535623\n",
    "3255245654254\n",
    "3446585845452\n",
    "4546657867536\n",
    "1438598798454\n",
    "4457876987766\n",
    "3637877979653\n",
    "4654967986887\n",
    "4564679986453\n",
    "1224686865563\n",
    "2546548887735\n",
    "4322674655533\n",
]

UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

def dirToStr(dir):
    if dir == UP:
        return "UP"
    elif dir == DOWN:
        return "DOWN"
    elif dir == LEFT:
        return "LEFT"
    elif dir == RIGHT:
        return "RIGHT"
    
def getNeigh(grid: [str], current : (int,int)) -> [((int,int),(int,int))]:
    up = (current[0] + UP[0], current[1] + UP[1])
    down = (current[0] + DOWN[0], current[1] + DOWN[1])
    left = (current[0] + LEFT[0], current[1] + LEFT[1])
    right = (current[0] + RIGHT[0], current[1] + RIGHT[1])

    neigh = [(up,UP), (down,DOWN), (left,LEFT), (right,RIGHT)]
    ret = []

    for (x,y),dir in neigh:
        if 0 <= x < len(grid[0]) and 0 <= y < len(grid):
            ret.append(((x,y),dir))

    return ret

#D = open(sys.argv[1]).read().strip()
#L = D.split('\n')
#G = [[c for c in row] for row in L]

import heapq
def findWay(grid, start, end):
    part2= True
    Q = [(0,0,0,-1,-1)]
    D = {}
    R = len(grid)
    C = len(grid[0])

    while Q:
        dist,r,c,dir_,indir = heapq.heappop(Q)
        if (r,c,dir_,indir) in D:
            #assert dist >= D[(r,c,dir_,indir)]
            continue
        D[(r,c,dir_,indir)] = dist
        for i,(dr,dc) in enumerate([[-1,0],[0,1],[1,0],[0,-1]]):
            rr = r+dr
            cc = c+dc
            new_dir = i
            new_indir = (1 if new_dir!=dir_ else indir+1)

            isnt_reverse = ((new_dir + 2)%4 != dir_)

            isvalid_part1 = (new_indir<=3)
            isvalid_part2 = (new_indir<=10 and (new_dir==dir_ or indir>=4 or indir==-1))
            isvalid = (isvalid_part2 if part2 else isvalid_part1)

            if 0<=rr<R and 0<=cc<C and isnt_reverse and isvalid:
                cost = int(grid[rr][cc])
                heapq.heappush(Q, (dist+cost, rr,cc,new_dir,new_indir))

    ans = 1e9
    for (r,c,dir_,indir),v in D.items():
        if r==R-1 and c==C-1:
            ans = min(ans, v)
    return ans

"""
def findWay(grid : [str], start : (int,int), end : (int,int)):

    toScan = set()
    table = {}
    scanned = set()

    #for y in range(len(grid)):
    #    for x in range(len(grid[0])):
    #        toScan.append((x,y))
    table[start] = (0,start, ((0,0),0))
    toScan.add(start)

    while toScan:

        lowest = (0,0),float("inf"), ((0,0), 0)
        for p in toScan:
            if p in table:
                cost,_ ,d  = table[p]
                if lowest[1] > cost:
                    lowest = (p, cost, d)
        
        curP, curCost, (curDir, curCount) = lowest

        if curP in scanned:
            if curP in toScan:
                toScan.remove(curP)             
            continue

        print(f"{curP} {toScan} {scanned}")
        toScan.remove(curP)
        scanned.add(curP)
        #scanned.append(curP)
        #toScan.remove(curP)
        
        for (p, dir) in getNeigh(grid, curP):

            cost, _, _ = table.get(p, (float("inf"), curP, (dir, 1)))
            newCost = curCost + int(grid[p[1]][p[0]])
            reverse = curDir == (dir[0] * (-1), dir[1] * (-1))

            inDir = 1 if curDir != dir else curCount + 1
            
            if reverse:
                #print("- Tried to go backwards")
                continue

            toScan.add(p)

            if newCost < cost:
                if curDir == dir:
                    if inDir <= 3:
                        table[p] = (newCost, curP, (dir, (curCount + 1)))
#                        print(f"NEXT {p} {table[p]} | {curDir}")
                    else:
                        print(f"TOO LONG IN ONE DIRECTION {curP} {dirToStr(dir)} {p}")
                        continue
                elif curDir != dir:
                    table[p] = (newCost, curP, (dir, 1))
  #                  print(f"NEW {p} {table[p]} ")
                elif inDir >= 3:
                    print("ERROR")
                    exit()
                else:
                    print("ERROR 2")
                    exit()
        
        #print(f"current: {curP} -> {table}")

    for p in table:
        print(f"{p} -> {table[p]}")

    print("-------")

    path = []
    cur = end
    while cur != start:
        t = cur
        _, cur, (dir, c) = table[cur]
        path.append((t,dir,c))
    
    path.reverse()

    l = [ p for (p,_,_) in path]
    
    for (p,dir,c) in path:
        print(f"{p}  \t{dirToStr(dir)}\t{c}")

    print("----------")
    print(l)

    print("----------")
    for ((x,y), dir, c) in path:
        line = list(grid[y])
        char = "."
        line[x] = char
        grid[y] = "".join(line)

    for line in grid:
        print(line)

    (heat, _, _) = table[end]
    #print(f">{table[end]}<")

    return heat
"""
def doIt(data : [str]) -> int:

    for i in range(len(data)):
        data[i] = data[i].strip()    

    start = (0,0)
    end = (len(data[0]) - 1, len(data) - 1)
    
    way = findWay(data, start, end)

    ans = way
    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 17\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 1_051 Too High
    # 1_004 CV Paste
    # Part 2
    # 1_171 CV Paste
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()