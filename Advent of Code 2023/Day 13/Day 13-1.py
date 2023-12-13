testData = [
    "#.##..##.\n",
    "..#.##.#.\n",
    "##......#\n",
    "##......#\n",
    "..#.##.#.\n",
    "..##..##.\n",
    "#.#.##.#.\n",
    "\n",
    "#...##..#\n",
    "#....#..#\n",
    "..##..###\n",
    "#####.##.\n",
    "#####.##.\n",
    "..##..###\n",
    "#....#..#\n",
]

#from enum import Enum
#class Dir(Enum):
#    VERTICAL = 0,
#    HORIZONTAL = 1,
#    NONE = 2,
#    def __repr__(self):
#        return f"{self.name}"

def checkHori(room, i) -> bool:
    #print(f"{room} | {i}")
    a = i
    b = i + 1
    l = len(room)

    while a >= 0 and b < l:
        #print(f"--")
        #print(f"{room[a]} -> {a}")
        #print(f"{room[b]} -> {b}")
        #print(room[a] == room[b])
        if room[a] == room[b]:
            a -= 1
            b += 1
        else:
            return False
   
    return True

def checkVert(room, i) -> bool:
    a = i
    b = i + 1
    l = len(room[0])

    while a >= 0 and b < l:
        #print(f"{a} {b} {l}")
        lA = [line[a] for line in room]
        lB = [line[b] for line in room]
        #print(f"{lA}")
        #print(f"{lB}")
        if lA == lB:
            a -= 1
            b += 1
        else:
            return False
   
    return True

def checkMirror(room : [str]) -> int:
 
    note = 0
    rows = len(room)
    
    for i in range(rows):
        if i + 1 < rows:
            if room[i] == room[i+1]:
                #print("HORIZONTAL {a} {b}")
                if checkHori(room, i):
                    ret = (i + 1) * 100
                   #print(f"IT IS HORIZONTAL {i} {ret}")
                    return ret

    col = len(room[0])
    for i in range(col):
        if i + 1 < col:
            a = [line[i] for line in room]
            b = [line[i+1] for line in room]
            #print(f"a -> {a} {i}")
            #print(f"b -> {b} {i+1}")
            if a == b:
                #print(f"VERTICAL {room[i]} {room[i+1]}")
                if checkVert(room, i):
                    ret = i + 1
                    #print(f"IT IS VERTICAL {i} {ret}")
                    return ret

    return note

def doIt(data : [str]) -> int:
    rooms = []

    room = []
    while data:
        line = data.pop(0)
        if line == "\n":
            #rooms.append((room, Dir.NONE))
            rooms.append(room)
            #print(f"ROOM {room}")
            room = []
            continue
        room.append(line.strip())
        #print(f"ROOM {room}")
    rooms.append(room)
    
    i = 0
#    for (r,dir) in rooms:
    #for r in rooms[:1]:
#        print(f"Room {i}: {dir}")
    #    print(f"Room {i}:")
    #    for line in r:
    #        print(f"{line}")
    #    print("-----------------------")
    #    i += 1

    ans = 0

    i = 0
    for r in rooms:
        #print(r)
        #print(i)
        i +=1
        ans += checkMirror(r)

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 13\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 29_846 First Try :)
    # Part 2
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()