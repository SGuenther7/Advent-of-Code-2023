#testData = [
#    ".|...\....",
#    "|.-.\.....",
#    ".....|-...",
#    "........|.",
#    "..........",
#    ".........\",
#    "..../.\\..",
#    ".-.-/..|..",
#    ".|....-|.\",
#    "..//.|....",
#]

testData2 = [
    ".|...\\....\n",
    "|.-.\\.....\n",
    ".....|-...\n",
    "........|.\n",
    "..........\n",
    ".........\\\n",
    "..../.\\\\..\n",
    ".-.-/..|..\n",
    ".|....-|.\\\n",
    "..//.|....\n",
]

energized = set()
#energized = list()

UP    = ( 0,-1)
DOWN  = ( 0, 1)
LEFT  = (-1, 0)
RIGHT = ( 1, 0)

def dirToStr(dir):
    if dir == UP:
        return "UP"
    elif dir == DOWN:
        return "DOWN"
    elif dir == LEFT:
        return "LEFT"
    elif dir == RIGHT:
        return "RIGHT"
    
def goDir(cur, dir):
    #print(f"\t{cur}\t{dirToStr(dir)} {dir}")
    #energized.append((cur,dir))
    energized.add((cur,dir))
    return (cur[0] + dir[0], cur[1] + dir[1])
        
def walk(data : [str], curPos : (int,int), goto : (int,int), currentDepth = 0, inTest = False):
    curX, curY = curPos
    dir = goto
    alreadyIn = inTest
    depth = currentDepth

    while True:
        depth += 1

        #if depth >= 2000:
        #    print("LIMIT REACHED")
        #    break
        
        if curX < 0 or curX >= len(data[0]) or curY < 0 or curY >= len(data):
            #print(f"WALL {(curX,curY)}")
            return
        
#        print(f"{((curX,curY),dir)} -> {energized}")

        if ((curX,curY), dir) in energized:
            if alreadyIn: 
               # print(f"breaked on {(curX,curY)} {dirToStr(dir)}")
                return
                break
            else:
                #print(f"already in {(curX,curY)} {dirToStr(dir)}")
                alreadyIn = True
        else:
            alreadyIn = False
        
        #energized.add(((curX,curY),dir))
        #energized.append(((curX,curY),dir))
        currentC = data[curY][curX]
        
#        print(f"> {currentC} <\t{(curX,curY)}\t{dirToStr(dir)}\t{dir}\t{len(energized)}")
        #print(f"-> before {(curX,curY)} \t{currentC} {alreadyIn}")

        #sleep(0.1)

        if currentC == ".":
            #walk(data, (nextX,nextY), dir)
            #print(f"----- . before {(curX,curY)}")
            curX, curY = goDir((curX,curY), dir)
            #print(f"----- . after {(curX,curY)}")
 
        elif currentC == "|":
            if dir == UP or dir == DOWN:
                #walk(data, (nextX,nextY), dir)
                curX, curY = goDir((curX,curY), dir)
            else:
                aX, aY = goDir((curX, curY), UP)
                walk(data, (aX, aY), UP, depth, alreadyIn)
                #walk(data, (nextX,nextY), (0, 1))
                dir = DOWN
                curX, curY = goDir((curX,curY), dir)
            
        elif currentC == "-":
            if dir == LEFT or dir == RIGHT:
                #walk(data, (nextX,nextY), dir)
                curX, curY = goDir((curX,curY), dir)
            else:
                aX, aY = goDir((curX, curY),LEFT)
                walk(data, (aX, aY), LEFT, depth, alreadyIn)
                #walk(data, (curX + LEFT[1], curY + LEFT[0]), LEFT, depth)
                #walk(data, (nextX,nextY), (1,0))
                dir = RIGHT
                curX, curY = goDir((curX,curY), dir)
           
        elif currentC == "/":
            if dir == RIGHT: # going right
                #walk(data, (nextX,nextY), (0,-1)) # go up
                dir = UP
                curX, curY = goDir((curX,curY), dir)
            elif dir == LEFT: # going left
                #walk(data, (nextX,nextY), (0,1))  # go down
                dir = DOWN
                curX, curY = goDir((curX,curY), dir)
            elif dir == DOWN: # going down
                #walk(data, (nextX,nextY), (-1,0)) # go left
                dir = LEFT
                curX, curY = goDir((curX,curY), dir)
            elif dir == UP: # going up
#                walk(data, (nextX,nextY), (1,0))  # go right
                dir = RIGHT
                curX, curY = goDir((curX,curY), dir)
        
        elif currentC == "\\":
            if dir == RIGHT: # going right
#                walk(data, (nextX,nextY), (0,1))  # go down
                dir = DOWN
                curX, curY = goDir((curX,curY), dir)
            elif dir == LEFT: # going left
#                walk(data, (nextX,nextY), (0,-1)) # go up
                dir = UP
                curX, curY = goDir((curX,curY), dir)
            elif dir == DOWN: # going down
#                walk(data, (nextX,nextY), (1,0))  # go right
                dir = RIGHT
                curX, curY = goDir((curX,curY), dir)
            elif dir == UP: # going up
#                walk(data, (nextX,nextY), (-1,0)) # go left
                dir = LEFT
                curX, curY = goDir((curX,curY), dir)
        else:
            print(f">>>> ERROR <<<< {(curX, curY)} {data[curY]}")
            return
        #print(f"-> after {(curX,curY)} \t{currentC} {alreadyIn}")

def doRun(data : [str], start: (int,int), dir : (int,int)) -> int:
    grid = list(data)
  #  print(f"RUN: {start} {dirToStr(dir)}")
    
    walk(grid, start, dir)
    
    for i in range(len(grid)):
        grid[i] = list(grid[i])

    for ((x,y),dir) in energized:
        #print(f"{(x,y)} {dirToStr(dir)} {dir} {data[y][x]}")
        grid[y][x] = "#"

    for i in range(len(grid)):
        grid[i] = "".join(grid[i])
    
    energy = 0
    for line in grid:
        energy += line.count("#")
        #print(line)

    #print(energy)
    energized.clear()

    return energy

def doIt(data : [str]) -> int:

    print("-----------------")
    for i in range(len(data)):
        data[i] = data[i].strip()

    #for line in data:
    #    print(f"{line} -> {len(line)}")
    

    #walk(data, (0,0), RIGHT)
    
#    for i in range(len(data)):
#        data[i] = list(data[i])
#
#    for ((x,y),dir) in energized:
#        #print(f"{(x,y)} {dirToStr(dir)} {dir} {data[y][x]}")
#        data[y][x] = "#"
#    #for y in range(len(data)):
#    #    for x in range(len(data[y])):
#    #        if data[y][x] != "#":
#    #            data[y][x] = "."
#
#    for i in range(len(data)):
#        data[i] = "".join(data[i])
#
#    print("-----------\n")
#    energy = 0
#    for line in data:
#        energy += line.count("#")
#        print(line)
#
#    print(f"len: {len(energized)} | # : {energy}")
        
    ans = 0
    runParams = [
#       startPoint,        change, direction, length
        ((0,0),            (1,0),  DOWN,      len(data[0])), #   FROM ABOVE
        ((len(data[0]),0), (0,1),  LEFT,      len(data)), #   FROM RIGHT
        ((0,len(data)),    (1,0),  UP,        len(data[0])), #   FROM UNDERSIDE
        ((0,0),            (0,1),  RIGHT,     len(data)) #   FROM LEFT
                 ]

    for ((startX,startY), (changeX,changeY), dir, length) in runParams:
        posX = startX
        posY = startY

        for i in range(length):
            #print(f"{(posX, posY)} {dirToStr(dir)}")

            energy = doRun(data, (posX, posY), dir)

            if energy > ans:
                ans = energy

            posX += changeX
            posY += changeY
    
    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 16\input.txt", 'r')

    data = file.readlines() 
    #data = testData
    #data = testData2

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 8_539 First Try
    # Part 2
    # 8_674 First Try
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()
