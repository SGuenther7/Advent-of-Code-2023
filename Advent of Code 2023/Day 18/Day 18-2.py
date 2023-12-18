testData = [
    "R 6 (#70c710)\n",
    "D 5 (#0dc571)\n",
    "L 2 (#5713f0)\n",
    "D 2 (#d2c081)\n",
    "R 2 (#59c680)\n",
    "D 2 (#411b91)\n",
    "L 5 (#8ceee2)\n",
    "U 2 (#caa173)\n",
    "L 1 (#1b58a2)\n",
    "U 2 (#caa171)\n",
    "R 2 (#7807d2)\n",
    "U 3 (#a77fa3)\n",
    "L 2 (#015232)\n",
    "U 2 (#7a21e3)\n",
]

def getOffSet(dir, length):
    x = 0
    y = 0

    if dir == "R":
        x = 1
    elif dir == "D":
        y = 1
    elif dir == "L":
        x = -1
    elif dir == "U":
        y = -1
    
    return (x * length, y * length)

def coordsToLine(xs : [int]) -> str:
    #print(f"{x}")
    #xs = list(set(xs))
   # print(f"xs : {xs}")
    #xs.sort()
   # print(f"-- {xs}")
    #line = ["." for i in range(xs[-1] + 1)]
    line = ["." for i in range(max(xs) + 1)]
  #  print(f"-- {line}")

    for x in xs:
        line[x] = "#"

    return "".join(line)

def createGrid(lines, startP) -> [str]:
    grid = {}
    current = startP

    print("creating grid")
    for (dir, length) in lines:
        #print(f"---")
        #print(f"cmd: {dir} {length} {current}")
        off = getOffSet(dir, length)
        end = (off[0] + current[0], off[1] + current[1])
        #print(f"off: {off} | cur: {current} | end: {end}")

        for y in range(abs(off[1]) + 1):
            
            l = grid.get(y + current[1] + (off[1] if off[1] < 0 else 0), [])
            new = [current[0] + x + (off[0] if off[0] < 0 else 0) for x in range(abs(off[0]) + 1)]
            
            l += new
            
            grid[y + current[1] + (off[1] if off[1] < 0 else 0)] = l
            #print(f"-> {(current[0] + off[0], (y + current[1]))}")

        #print("---------")
       # print(f"end: {end}")
        current = end
        #print("\n")

    #print("\ngrid:")
    #print(grid)
    print("---------")

    #keys = grid.keys()
    #keys.sort()

    #print(f"lines: {grid.keys()} {keys[-1]} {startP[1]}")
    print("Coordinates to Strings")
    grid2 = [[] for y in range(len(grid))]
    for y in grid:
        #print(f"{y} -> {grid[y]}")
        grid2[y] = coordsToLine(grid[y])

#    for line in grid2:
#        #if line != []:
#        print(line)
#        #print(f"{"".join(line)}")
#        #print(type(line))

    grid = []
# paint
    print("Colouring the Grid")
    for y in range(len(grid2)):
        inside = False
        string = ""

        connectUP = 0
        connectDOWN = 0

        #print(grid2[y])
        for x in range(len(grid2[y])):
            char = grid2[y][x]
           # print(f"{x} {y}")

            if char == "#":
                if y + 1 < len(grid2):
                    if len(grid2[y + 1]) > x:
                        if grid2[y + 1][x] == "#":
                            connectDOWN += 1
                if y - 1 >= 0:
                    if len(grid2[y - 1]) > x:
                        if grid2[y - 1][x] == "#":
                            connectUP += 1

            inside = connectDOWN % 2 == 1 and connectUP % 2 == 1
            
            if char == ".":
                if inside:
                    string += "0"
                else:
                    string += char
            else:
                string += char
        grid.append("".join(string))

#    for line in grid:
#        #if line != []:
#        print(line)
#        #print(f"{"".join(line)}")
#        #print(type(line))

    print("Counting")
    border = 0
    inside = 0
    for line in grid:
        border += line.count("#")
        inside += line.count("0")

    #print(f"border: {border}")
    #print(f"inside: {inside}")
    #print(f"both:   {border + inside}")    

    return border + inside

def doIt(data : [str]) -> int:

    print("-------\n")
    cmds = []

    startX = 0
    curX = 0
    maxX = 0

    startY = 0
    curY = 0
    maxY = 0

    aboveCounted = False

    dirFromInt = {"0":"R", "1":"D", "2":"L", "3":"U"}
    iter = 0
    for line in data:
        dirOLD, lengthOLD, colorOLD = line.strip().split()
        
        _, data = colorOLD.split("#")
        dir = dirFromInt[data[5]]
        length = int(data[:5], 16)

        #print(f"{dir} {length}")
        cmds.append((dir, int(length)))

        if not aboveCounted:
            l = int(length)
            #print(f"-- {iter} cmd: {dir} {l}")
            if dir == "U":
                curY -= l
            elif dir == "D":
                curY += l
            elif dir == "R":
                curX += l
            elif dir == "L":
                curX -= l
            #print(f"-- {iter} current: {(curX, curY)} {(startX,startY)}")

            if startY > curY:
                startY = curY
            if startX > curX:
                startX = curX
            
            if maxX < curX:
                maxX = curX
            if maxY < curY:
                maxY = curY
        iter += 1

    start = (abs(startX), abs(startY))
    print(f"start: {startX} {startY} -> {start} | max: {(abs(startX) + maxX, abs(startY) + maxY)}")
    
    for (dir, length) in cmds:
        print(f"{dir} {length}")
    ans = 0
    ans = createGrid(cmds[:], start)

    return ans    

from time import process_time, sleep
import datetime

def main():
    file = open("..\Python\Advent of Code 2023\Day 18\input.txt", 'r')

    data = file.readlines() 
    data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 48_400 First Try
    # Part 2
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()