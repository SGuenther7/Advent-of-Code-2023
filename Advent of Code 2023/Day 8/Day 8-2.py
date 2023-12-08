testData = [
    "RL",
    "",
    "AAA = (BBB, CCC)",
    "BBB = (DDD, EEE)",
    "CCC = (ZZZ, GGG)",
    "DDD = (DDD, DDD)",
    "EEE = (EEE, EEE)",
    "GGG = (GGG, GGG)",
    "ZZZ = (ZZZ, ZZZ)",
]

testData2 = [
    "LLR",
    "",
    "AAA = (BBB, BBB)",
    "BBB = (AAA, ZZZ)",
    "ZZZ = (ZZZ, ZZZ)",
]

testData3 = [
    "LR",
    "",
    "11A = (11B, XXX)",
    "11B = (XXX, 11Z)",
    "11Z = (11B, XXX)",
    "22A = (22B, XXX)",
    "22B = (22C, 22C)",
    "22C = (22Z, 22Z)",
    "22Z = (22B, 22B)",
    "XXX = (XXX, XXX)",
]

def doIt(data):
    moves, _, mapD = data[0], data[1], data[2:]
    
    for mov in moves:
        print(f"|{mov}|")

    if moves[-1] == "\n":
    #    print(f"|{moves[-1]}|")
        moves = moves[0:-1]

    print("___________")

    for mov in moves:
        print(f"|{mov}|")

    current = []
    lookUp = {"L":{}, "R":{}}
    for line in mapD:
        cur, rest = line.split(" = ")
        left, right = rest[1:4], rest[6:9]

        lookUp["L"][cur] = left
        lookUp["R"][cur] = right
        
        if cur[-1] == "A": current.append(cur)
    
    print(moves)
    
    print( "current :->")
    for each in current:
        print(each)
    print("____")
    num_Moves = 0
    moveLength = len(moves)
    answer = []

    while current:
       
        go = moves[num_Moves % moveLength]
        
        lenght = len(current)
        for i in range(lenght):
            before = current[i]
            current[i] = lookUp[go][current[i]]
        num_Moves += 1

        cpy = current
        for elem in cpy:
            if elem.endswith("Z"):
                answer.append((elem, num_Moves))
                print(f"{elem} {num_Moves}")
                current.remove(elem)

#        num_of_end = sum(1 for elem in current if elem.endswith("Z"))

    print(answer)
    t = [ elem for st,elem in answer]
    num_Moves = 1
    for x in t:
        num_Moves = (x*num_Moves) // gcd(x, num_Moves)
 
    return num_Moves

from time import process_time, sleep
import datetime
from math import gcd 

def main():

    file = open("..\Python\Advent of Code 2023\Day 8\Day_8-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    #data = testData2
    #data = testData3
    
    t = process_time()
    print(datetime.datetime.now())    

    answer = doIt(data)

    print("----")
    print(answer)

# ['MJA', 'RGA', 'JMA', 'XHA', 'DQA', 'AAA']
#   HJZ HPZ FKZ PKZ ZZZ DHZ
#        152_000_000
#        820_000_000 238 | R | ['JXM', 'TGM', 'PPL', 'BQK', 'GCG', 'BBS'] | len:293 6
# 21_003_205_388_413
    elapsed_time = process_time() - t
    print(f"Start: {(datetime.timedelta( seconds=( elapsed_time ) ) )}")

    # 19631

if __name__ == "__main__":
    main()