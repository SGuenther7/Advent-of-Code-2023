testData = [
    "7-F7-",
    ".FJ|7",
    "SJLL7",
    "|F--J",
    "LJ.LJ",
]
testData2 = [
    "...........",
    ".S-------7.",
    ".|F-----7|.",
    ".||.....||.",
    ".||.....||.",
    ".|L-7.F-J|.",
    ".|..|.|..|.",
    ".L--J.L--J.",
    "...........",
]
testData3 = [
    ".F----7F7F7F7F-7....",
    ".|F--7||||||||FJ....",
    ".||.FJ||||||||L7....",
    "FJL7L7LJLJ||LJ.L-7..",
    "L--J.L7...LJS7F-7L7.",
    "....F-J..F7FJ|L7L7L7",
    "....L7.F7||L7|.L7L7|",
    ".....|FJLJ|FJ|F7|.LJ",
    "....FJL-7.||.||||...",
    "....L---J.LJ.LJLJ...",
]
testData4 = [
    "FF7FSF7F7F7F7F7F---7",
    "L|LJ||||||||||||F--J",
    "FL-7LJLJ||||||LJL-77",
    "F--JF--7||LJLJIF7FJ-",
    "L---JF-JLJIIIIFJLJJ7",
    "|F|F-JF---7IIIL7L|7|",
    "|FFJF7L7F-JF7IIL---7",
    "7-L-JL7||F7|L7F-7F7|",
    "L.L7LFJ|||||FJL7||LJ",
    "L7JLJL-JLJLJL--JLJ.L",
]

from enum import Enum
class Dir(Enum):
    UP = 0,
    DOWN = 1,
    LEFT = 2,
    RIGHT = 3,
    START = 4
    def __repr__(self):
        return f"{self.name}"
    
#       (7,|,F)      #
#  (L,-,F) S (7,-,J) # 
#       (J,|,L)      #

#     J | L
#     - S -
#     7 | F

connectorDOWN  = "7|FS"
connectorRIGHT = "F-LS"
connectorLEFT  = "7-JS"
connectorUP    = "J|LS"

validUP    = {"S":connectorDOWN,  "|":connectorDOWN,  "L":connectorDOWN,  "J":connectorDOWN}
validRIGHT = {"S":connectorLEFT,  "-":connectorLEFT,  "L":connectorLEFT,  "F":connectorLEFT}
validDOWN  = {"S":connectorUP,    "|":connectorUP,    "F":connectorUP,    "7":connectorUP}
validLEFT  = {"S":connectorRIGHT, "-":connectorRIGHT, "7":connectorRIGHT, "J":connectorRIGHT}

validDir = {Dir.UP:validUP, Dir.RIGHT:validRIGHT, Dir.DOWN:validDOWN, Dir.LEFT:validLEFT}

def is_valid_Dir(start : str, next : str, dir : Dir) -> bool :
    d = validDir[dir].get(start, [])
    ret = next in d
    #print(f"{start} {dir.name} {next} = {ret} | {d}")
    return ret

def get_next_coor(data, startXY: (), clockwise = True):

    char, startX, startY, wentDIR = startXY

    indices = [(startX, startY-1, Dir.UP), (startX+1, startY, Dir.RIGHT), (startX, startY+1, Dir.DOWN), (startX-1, startY, Dir.LEFT)]

    if not clockwise: indices.reverse()

    ret = indices

    for (x,y, dir) in indices:
        if x < 0 or y < 0 or x >= len(data[y]) or y >= len(data):
            ret.remove((x,y, dir))
    
    next = ()

    for x,y,dir in ret:
        test = is_valid_Dir(data[startY][startX], data[y][x], dir)
        #print(f"TEST : {test}")
        if test:
            return (data[y][x], x, y, dir)    

next_DIR = {
    ("|",Dir.UP):Dir.UP, ("|",Dir.DOWN):Dir.DOWN,
    ("-",Dir.RIGHT):Dir.RIGHT, ("-",Dir.LEFT):Dir.LEFT,
    ("F",Dir.UP):Dir.RIGHT, ("F",Dir.LEFT):Dir.DOWN,
    ("L",Dir.DOWN):Dir.RIGHT, ("L",Dir.LEFT):Dir.UP,
    ("J",Dir.DOWN):Dir.LEFT, ("J",Dir.RIGHT):Dir.UP,
    ("7",Dir.RIGHT):Dir.DOWN, ("7",Dir.UP):Dir.LEFT,
}

offset_DIR = {
    Dir.UP:    (0,-1),
    Dir.RIGHT: (1, 0),
    Dir.DOWN:  (0, 1),
    Dir.LEFT: (-1, 0),
}

def go_Next(data, elem):
    char, x, y, dir_before = elem
    nextDir = next_DIR[(char,dir_before)]
    
    (offsetX, offsetY) = offset_DIR[nextDir]
    nextX = x + offsetX
    nextY = y + offsetY
    return (data[nextY][nextX], nextX, nextY, nextDir)

def extract_Loop(data):
    y = 0
    x = 0

    while "S" not in data[y]: 
        #print(f"|{data[y][-1]}|")
        y += 1
    while "S" != data[y][x]: x += 1
    
    #print(f"{data[y]} {y} {x}")

    loop =[("S", x, y, Dir.START)]
    loop.append(get_next_coor(data, loop[0], True))
    
    #print(next)

    while loop[-1][0] != "S":
        #print(f"{loop[-1]} | {loop[-1][0]}")
        loop.append(go_Next(data, loop[-1]))

    clean = []
    print(f"lines: {len(data)} | rows: {len(data[0])}")
    for newY in range(len(data)):
        line = "".join(["." for i in range(len(data[0]))])
        #print(f"line: {line}")
        clean.append(line)

    for (char, x, y, _) in loop:
        temp = list(clean[y])
        temp[x] = char
        clean[y] = "".join(temp)

    #for line in clean:
    #    print(line)
    #print("Filling Inside")

    loop = []
    for line in clean:
        string = ""
        
        inside = False
        i = 0

        connectUP = 0
        connectDOWN = 0

        for char in line:
            #print(f"string|{string}| {type(string)}")

            if char == "F" or char == "7":
                connectDOWN += 1
            elif char == "J" or char == "L":
                  connectUP += 1
            elif char == "|":
                connectDOWN += 1
                connectUP += 1
                        #
            inside = connectDOWN % 2 == 1 and connectUP % 2 == 1
            
            if char == ".":
                if inside:
                    string += "0"
                else:
                    string += char
            else:
                string += char
                

        #print(f"string: {string}")
        loop.append("".join(string))
#        for in range(len(line)):

    print("")
    #for line in clean:
    #    loop.append("".join(line))

    #for line in loop:
    #    print(line)
 
    return loop

def doIt(data):
    loop = extract_Loop(data)
    
    #print(loop)

    accum = 0
    for line in loop:
        accum += line.count("0")

    return accum

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 10\input.txt", 'r')

    data = file.readlines() 
    #data = testData
    #data = testData2
    #data = testData3
    #data = testData4

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 6649 First Try :)

    # Part 2
    # 979 too High
    # 601

    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()