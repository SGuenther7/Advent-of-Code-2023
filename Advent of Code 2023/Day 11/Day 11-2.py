testData =  [
    "...#......",
    ".......#..",
    "#.........",
    "..........",
    "......#...",
    ".#........",
    ".........#",
    "..........",
    ".......#..",
    "#...#.....",
]

#       ....#........
#       .........#...
#       #............
#       .............
#       .............
#       ........#....
#       .#...........
#       ............#
#       .............
#       .............
#       .........#...
#       #....#.......

import math
factor = 1_000_000

def expand(galax):
    expandedLINE = []

    print("- LINES")
    for line in galax:
        line.strip()
        if "#" not in line:
            for i in range(factor - 1):
                expandedLINE.append(line)
        expandedLINE.append(line)
            
    expanded = [ [] for line in expandedLINE]

    print("- COLUMNS")
    expansion = "".join([ "#" for _ in range(factor)])
    #print(expansion)
    length = len(expandedLINE[0])
    for i in range(len(expandedLINE[0])):
        if all(line[i] == "." for line in expandedLINE):
            for y in range(len(expandedLINE)):
                expanded[y] += expansion
                #for _ in range(factor):
                #    expanded[y] += expandedLINE[y][i]
        else:
            for y in range(len(expandedLINE)):
                expanded[y] += expandedLINE[y][i]

    for i in range(len(expanded)):
        expanded[i] = "".join(expanded[i])

    return expanded

def getDistance(galax, a, b):
    d = 0
    (ax, ay) = a
    (bx, by) = b
    
    #print(f"----- {a} {b} | {(by - ay)} {(bx - ax)}")
    vertDistOff = abs(by - ay)
    vertDist = 0
    for i in range(vertDistOff):
        index = min(ay, by) + i
        #print(f"{index} {i}")
        if "#" not in galax[index]:
            #print(f"empty line {index}")
            vertDist += factor    
        else:
            vertDist += 1
    
    horiDistOff = abs(bx - ax)
    horiDist = 0
    for i in range(horiDistOff):
        index = min(ax, bx) + i
        #print(f"{index} {by} {horiDistOff} {i} ")
        if all(line[index] == "." for line in galax):           
            #print(f"empty col {index}") 
            horiDist += factor    
        else:
            horiDist += 1

    d = vertDist + horiDist
    return d

def extractGalax(galax):
    points = []
    num = 1
    
    for y in range(len(galax)):
    #for line in galax:
        indices = [i for i, ltr in enumerate(galax[y]) if ltr == "#"]
        #print(f"line {y} : {indices}")
        for indice in indices:
            points.append((indice, y))
            num += 1
    return points

def getDistances(galax, points):
    starts = []
    distances = []

    for startPoint in points:
        starts.append(startPoint)
        for p in points:
            if p not in starts:
                #d = getDistance(startPoint, p)
                d = getDistance(galax, startPoint, p)
                distances.append((startPoint, p, d))

    return distances

def doIt(data):
    
    clean = []
    for line in data:
        clean.append(line.strip())

    data = clean
    #for line in data:
    #    print(line)

    #print("Expanding")
    #expanded = expand(data)            

    #for line in expanded:
    #    print(line)

    print("Pointing")
    galaxPoints = extractGalax(clean)

    #for point in galaxPoints:
    #    print(point)

    print("distancing")
   
    distances = getDistances(clean, galaxPoints)

    minDist = sum([d for (_,_,d) in distances])
    #for (a,b,d) in distances:
    #    print(f"{a} -> {b} : {d}")

    print(len(distances))

    ans = minDist
   
    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 11\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    #print(f"d: {getDistance((7, 12),(10, 9))}")

    # Part 1
    #  7_076_090 too Low
    # 10_173_804
    # Part 2
    # 82_000_210 Too Low (war testData -_-)
    # 634_324_905_172 
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()