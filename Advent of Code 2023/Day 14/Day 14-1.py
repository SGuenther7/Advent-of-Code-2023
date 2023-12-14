testData = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

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

def doIt(data : [str]) -> int:
    
    ans = 0

    counts = []
    #print(f"{len(data)} {len(data[0])}")
    #c = 0
    #for line in data:
    #    print(f"{c} - {line}")
    #    c += 1


    for i in range(len(data[0].strip())):
        #print(f"-- {i}")
        col = [line[i] for line in data]
        counts += countCol(col)

    #print(counts)

    for (highest, length) in counts:
        #print(f"{highest} {type(highest)} {length} {type(length)}")
        for i in range(length):
            ans += highest - i

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
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()