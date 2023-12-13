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

allowed_Smudges = 1
#testROOM = 2

def checkHori(room, i) -> bool:
    #print(f"{room} | {i}")
    a = i
    b = i + 1
    l = len(room)
    dist = 0
    while a >= 0 and b < l:
       #print(f"--")
       #print(f"{room[a]} -> {a}")
       #print(f"{room[b]} -> {b}")
       #print(room[a] == room[b])
        dist += lev(room[a], room[b])
        if dist <= allowed_Smudges:
        #if room[a] == room[b]:
            a -= 1
            b += 1
        else:
            return False
   
    return dist == allowed_Smudges

def checkVert(room, i) -> bool:
    a = i
    b = i + 1
    l = len(room[0])
    dist = 0
    while a >= 0 and b < l:
        #print(f"{a} {b} {l}")
        lA = "".join([line[a] for line in room])
        lB = "".join([line[b] for line in room])
        #print(f"{lA}")
        #print(f"{lB}")
        dist += lev(lA,lB)
        if dist <= allowed_Smudges:
        #if lA == lB:
            a -= 1
            b += 1
        else:
            return False
   
    return dist == allowed_Smudges

def checkMirror(room : [str]) -> int:
 
    note = 0
    rows = len(room)
    
    for i in range(rows):
        if i + 1 < rows:
            dist = lev(room[i], room[i+1])
            if dist <= allowed_Smudges:
            #if dist == 1 or dist == 0:
            #if room[i] == room[i+1]:
                #print(f"HORIZONTAL {room[i]} {room[i+1]} {dist}")
                if checkHori(room, i):
                    ret = (i + 1) * 100
                    #print(f"IT IS HORIZONTAL {i} {ret}")
                    return ret

    col = len(room[0])
    for i in range(col):
        if i + 1 < col:
            a = "".join([line[i] for line in room])
            b = "".join([line[i+1] for line in room])
            #print(f"a -> {a} {i}")
            #print(f"b -> {b} {i+1}")
            dist = lev(a, b)
            #print(f"VERT {dist} {a} {b}")
            if dist <= allowed_Smudges:
            #if dist == 1 or dist == 0:
            #if a == b:
                #print(f"VERTICAL {a} {b} {dist}")
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
    #for r in [rooms[testROOM]]:
    for r in rooms:
        #print(r)
        #print(i)
        i +=1
        ans += checkMirror(r)

    return ans    

from time import process_time, sleep
import datetime

#pip install python-Levenshtein
#from Levenshtein import distance as lev

from Levenshtein import distance as lev

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
    # 37_894 Too HIGH
    # 25_401
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()