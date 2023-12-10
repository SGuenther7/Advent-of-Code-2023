testData = [
    "7-F7-",
    ".FJ|7",
    "SJLL7",
    "|F--J",
    "LJ.LJ",
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
    
    #for x,y,dir in ret:
    #    print(f"{data[y][x]} |{x}|{y}| {dir.name}")

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
    #forward = loop
    #backward = loop

    loop.append(get_next_coor(data, loop[0], True))
    
    #print(next)

    while loop[-1][0] != "S":
        #print(f"{loop[-1]} | {loop[-1][0]}")
        loop.append(go_Next(data, loop[-1]))
        #sleep(0.25)

    #print(f"-- done {loop[-1]}")
    #print("____________")
    #print(len(loop))
    #print(loop)        

    return loop
    #get_next_coor(data, loop[0], False)
    #while True:

    #while True:
    #    cur, curX, curY = forward[-1]
    #    next = get_next_coor(data, (curX, curY), clockwise=True)
    #    if next[0] == "S": break
    #    forward.append(next)

    #while True:
    #    cur, curX, curY = backward[-1]
    #    next = get_next_coor(data, (curX,curY), clockwise=False)
    #    if next[0] == "S": break
    #    backward.append(next)

    pass

def doIt(data):
    loop = extract_Loop(data)
    
    #print(loop)
    
    middle = int(len(loop) / 2)
    
    print(middle)
    print(loop[middle])

    return middle    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 10\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # 6649 First Try :)

    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()