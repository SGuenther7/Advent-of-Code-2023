testData = [
    "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n"
]

boxes = {}

def getHash(word : str) -> int:
    h = 0
    
    for c in word:
        h = ((h + ord(c)) * 17) %256
    #print(h)
    return h

def dashFoo(cmd):
    label, lens = cmd.split("-")

    if lens == "": lens = 0
    else: lens = int(lens)

    h = getHash(label)
    print(f"DASH   {label} {lens} box:{h}")

    lenses = boxes.get(h, [])

    for i in range(len(lenses)):
        l, _ = lenses[i]
        if l == label:
            del lenses[i]
            break
    pass

def equalsSignFoo(cmd):
    label, lens = cmd.split("=")

    if lens == "": lens = 0
    else: lens = int(lens)

    h = getHash(label)
    print(f"EQUALS {label} {lens} box:{h}")
    
    lenses = boxes.get(h, [])

    inserted = False
    for i in range(len(lenses)):
        l, _ = lenses[i]
        if l == label:
            lenses[i] = (label, lens)
            inserted = True
            break

    if not inserted:
        lenses.append((label, lens))
    
    boxes[h] = lenses

    pass

def doIt(data : [str]) -> int:
    
    ans = 0
    words = data[0].strip().split(",")

    for w in words:
        #print(f"|{w}|")
        if "-" in w:
            dashFoo(w)
        elif "=" in w:
            equalsSignFoo(w)
        else:
            print("FAIL")

    for box in boxes:
        
        lenses = boxes[box]
        for i in range(len(lenses)):
            ans += (box + 1) * (i + 1) * lenses[i][1]
            #print(f"{box + 1} {}")
        #ans += (box + 1)
        
        #print(f"{box} -> {boxes[box]}")

    #ans += getHash(w)
    print(len(words))
    #print(getHash("HASH"))

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 15\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 504_036 First Try :)
    # Part 2
    # 295_719 First Try :)

    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()