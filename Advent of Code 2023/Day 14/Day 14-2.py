testData = [
    "O....#....\n",
    "O.OO#....#\n",
    ".....##...\n",
    "OO.#O....O\n",
    ".O.....O#.\n",
    "O.#..O.#.#\n",
    "..O..#O..O\n",
    ".......O..\n",
    "#....###..\n",
    "#OO..#....\n",
]

def tilt(line, reverse=False):
    line = "".join(line)
    
    lines = re.split("(#)", line)
    #print(lines)
    for i in range(len(lines)):
        lines[i] = list(lines[i])
        lines[i].sort(reverse=reverse)
    
    #for line in lines:
    #    print(lines)

    line = []
    for lin in lines:
        line += lin
 
    #print(f"- {line}")
    return line

def countCol(col : str) -> [(int, int)]:
    scores = []
    highest = len(col)
    cur = highest
    #print("_______________")
    #print(col)
    count = 0

    #for i in range(len(col))

    while col:
        c = col.pop(0)
        #print(c)
        if c == "O":
            count += 1
        elif c == "#":
            if count > 0:
                scores.append((highest, count))
            highest = cur - 1
            count = 0
        cur -= 1
    if count > 0:
        scores.append((highest, count))
            
    #print(f"{scores}")
    return scores

def getLoad(data):
    ans = 0
    #counts = []

    for i in range(len(data)):
        ans += data[i].count("O") *  (len(data) -i)
        #print(f"row {len(data) -i} {data[i].count("O")}")

    #for i in range(len(data[0])):
    #    #print(f"-- {i}")
    #    col = [line[i] for line in data]
    #    counts += countCol(col) *
#
    ##print(counts)
#
    #for (highest, length) in counts:
    #    #print(f"{highest} {type(highest)} {length} {type(length)}")
    #    for i in range(length):
    #        ans += highest - i

    return ans

import re
def countO(data):
    count = 0
    for line in data:
        count += line.count("O")
    return count
def doIt(data : [str]) -> int:
    
    ans = 0
    counts = []

    for i in range(len(data)):
        data[i] = list(data[i].strip())

    #for line in data:
    #    print(line)

    print("-------------")
    #cycles = 1
    cycles = 1_000_000_000
    scores = {}
    cycle = 0
    byGrid = {}

    while cycle < cycles:
        cycle += 1

        # tilt north
        for i in range(len(data[0])):
            col = [line[i] for line in data]
            #print(col)        
            col = tilt(col, True)
            #print(col)
            j = 0
            for c in col:
                data[j][i] = c
                j += 1
                
        #print(f"\nNORTH {cycle} {countO(data)}")
        #for line in data:
        #    print("".join(line))

        # tilt west
        for i in range(len(data)):
            row = data[i]
            trow = tilt(row, True)
            data[i] = trow
            #data[i] = tilt(data[i], True)
        
        #print(f"\nWEST {cycle} {countO(data)}")
        #for line in data:
        #    print("".join(line))

        # tilt south
        for i in range(len(data[0])):
            col = [line[i] for line in data]
            #print(col)        
            col = tilt(col, False)
            j = 0
            for c in col:
                data[j][i] = c
                j += 1

        #print(f"\nSOUTH {cycle} {countO(data)}")
        #for line in data:
        #    print("".join(line))
        
        # tilt east
        for i in range(len(data)):
           row = data[i]
           row = tilt(row, False)
           data[i] = row
           #data[i] = tilt(data[i], False)

        #print(f"\nEAST {cycle} {countO(data)}")
        #for line in data:
        #    print("".join(line))
 
        score = getLoad(data)
        t = scores.get(score, [])
        t.append(cycle)
        scores[score] = t

        #score = getLoad(data)
        #index = cycle % 100
        #t = cycleScores.get(index, [])
        #t.append(score)
        #cycleScores[index] = t

        if cycle % 10_000 == 0:
            print(f"- {cycle} {(cycle/cycles) * 100}%")

        #if not jumped and len(cycleScores) == 100:
        #    s = cycleScores[100 - 1]
        #    if len(s) > 10:
        #        print(f"Cycle {cycle} {t}")
        #        jumped = True

        grid = tuple(tuple(row) for row in data)
        
        if grid in byGrid :
            cycle_length = cycle - byGrid[grid]
            amt = (cycles - cycle) // cycle_length
            print(f"JUMPED {cycle} {cycle + amt * cycle_length} {cycle_length}")
            cycle += amt * cycle_length
            print(f"JUMPED {amt} {cycle_length}")

        byGrid[grid] = cycle

    
    for s in scores:
        print(f"score {s} -> {scores[s]}")
    print(scores.keys())

    for g in byGrid:
        print(f"{byGrid[g]}")

    print("\nAFTER")
    for line in data:
        print("".join(line))
 
    ## count north
    ans = getLoad(data)
    print(f"ITS: {ans}")
    return ans    



from time import process_time, sleep
import datetime

def main(): 

    file = open("..\Python\Advent of Code 2023\Day 14\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 107_430 First Try :)
    # Part 2
    # 96_317 zu viel debugging wegen copypaste
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()