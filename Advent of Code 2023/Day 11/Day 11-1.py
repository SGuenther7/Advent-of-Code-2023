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

def expand(galax):
    expandedLINE = []

    for line in galax:
        line.strip()
        if "#" not in line:
            expandedLINE.append(line)
        expandedLINE.append(line)
            
    expanded = [ [] for line in expandedLINE]

    length = len(expandedLINE[0])

    for i in range(len(expandedLINE[0])):
        if all(line[i] == "." for line in expandedLINE):
            for y in range(len(expandedLINE)):
                expanded[y] += expandedLINE[y][i]
                expanded[y] += expandedLINE[y][i]
        else:
            for y in range(len(expandedLINE)):
                expanded[y] += expandedLINE[y][i]

    for i in range(len(expanded)):
        expanded[i] = "".join(expanded[i])

    return expanded

def getDistance(a,b):
    (ax, ay) = a
    (bx, by) = b
    
    ans = (abs(bx - ax) + abs(by - ay))
    #print(f"({bx} - {ax}) + ({by}-{ay}) = {ans}")
    #print(f"({bx - ax}) + ({by - ay}) = {ans}")
    
    return ans

def extractGalax(galax):
    points = []
    num = 1
    
    for y in range(len(galax)):
    #for line in galax:
        indices = [i for i, ltr in enumerate(galax[y]) if ltr == "#"]
        #print(f"line {y} : {indices}")
        for indice in indices:
            points.append((y, indice))
            num += 1
    return points

def getDistances(points):
    starts = []
    distances = []

    for startPoint in points:
        starts.append(startPoint)
        for p in points:
            if p not in starts:
                d = getDistance(startPoint, p)
                distances.append((startPoint, p, d))

    return distances

def doIt(data):
    
    clean = []
    for line in data:
        clean.append(line.strip())

    data = clean
    #for line in data:
    #    print(line)

    print("Expanded")
    expanded = expand(data)            

    #for line in expanded:
    #    print(line)

    print("Pointed")
    galaxPoints = extractGalax(expanded)

    #for point in galaxPoints:
    #    print(point)

    print("distances")
   
    distances = getDistances(galaxPoints)

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
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()