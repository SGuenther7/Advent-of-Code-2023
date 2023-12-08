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

def doIt(data):
    moves, _, mapD = data[0], data[1], data[2:]
    
    if moves[-1] == "\n":
        moves = moves[0:-1]

    lookUp = {"L":{}, "R":{}}
    for line in mapD:
        cur, rest = line.split(" = ")
        left, right = rest[1:4], rest[6:9]

        lookUp["L"][cur] = left
        lookUp["R"][cur] = right
    
    current = "AAA"
    print( "current :-> " + current)

    num_Moves = 0
    while current != "ZZZ":
        if num_Moves >= 1_000_000_000_000: 
            print(f"stopped at {current} {num_Moves}")
            break
        
        elif num_Moves % 10_000_000 == 0:
            print(f"{num_Moves} {num_Moves % len(moves)} {current} | len:{len(moves)}")
        
        go = moves[num_Moves % len(moves)]
        
        current = lookUp[go][current]
                
        num_Moves += 1

    return num_Moves

from time import process_time
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 8\Day_8-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    #data = testData2
    
    t = process_time()
    print(datetime.datetime.now())    

    answer = doIt(data)

    print("----")
    print(answer)

    elapsed_time = process_time() - t
    print(f"Start: {(datetime.timedelta( seconds=( elapsed_time ) ) )}")

    # 19631

if __name__ == "__main__":
    main()