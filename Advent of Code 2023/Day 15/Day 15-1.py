testData = [
    "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7\n"
]


def getHash(word : str) -> int:
    h = 0
    
    for c in word:
        h = ((h + ord(c)) * 17) %256
    
    return h

def doIt(data : [str]) -> int:
    
    ans = 0
    words = data[0].strip().split(",")

    for w in words:
        #print(f"|{w}|")
        ans += getHash(w)

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
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()