testData = [
    "???.### 1,1,3\n",            # 1 arrangement
    ".??..??...?##. 1,1,3",     # 4 arrangements
    "?#?#?#?#?#?#?#? 1,3,1,6",  # 1 arrangement
    "????.#...#... 4,1,1",      # 1 arrangement
    "????.######..#####. 1,6,5",# 4 arrangements
    "?###???????? 3,2,1",       # 10 arran
]

cashed = {}

def walk(springs, nums, index, indexNum, cur):
    count = 0
    #print(f"{springs}|{nums}|{index}|{indexNum}|{cur}")
    key = (index, indexNum, cur)
    if key in cashed:
        return cashed[key]
    if index == len(springs):
        if indexNum == len(nums) and cur == 0:
            #print(f"A {indexNum} {len(nums)} {(len(nums)*5)} {cur}")
            return 1
        elif indexNum == len(nums)-1 and nums[indexNum] == cur:
            #print(f"B {indexNum} {len(nums)} {(len(nums)*5)} {cur}")
            return 1
        else:
            #print(f"0 {indexNum} {len(nums)} {(len(nums)*5)} {cur}")
            return 0

    for c in ['.', '#']:
        if springs[index] == c or springs[index] == '?':
            if c == '.' and cur == 0:
                count += walk(springs, nums, index+1, indexNum, 0)
            elif c == '.' and cur > 0 and indexNum < len(nums) and nums[indexNum] == cur:
                count += walk(springs, nums, index+1, indexNum+1, 0)
            elif c == '#':
                count += walk(springs, nums, index+1, indexNum, cur+1)
    cashed[key] = count
    return count

def countArrangements(line : str) -> int: 
    possible = 0
    #print(line)

    springs, nums = line.split(" ")

    # unfold
    
    #print(f"before: {springs}|{nums}")
    springs = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    #springs = "?".join([springs, springs, springs, springs, springs])
    nums = ",".join([nums, nums, nums, nums, nums])

    #print(f"after: {springs}|{nums}")
    
    nums = [int(x) for x in nums.split(',')]
    possible = walk(springs, nums, 0, 0, 0)
    #print(f"Possible: {possible}")

    return possible

def doIt(data : [str]) -> int:
    
    ans = 0
    
    #ans += countArrangements("????.??.??. 1,1".strip())
    #print(f"Line {i} Done")
    i = 0
    #for line in data[1:2]:
    for line in data:
        ans += countArrangements(line.strip())
       # print(f"Line {i} Done: {ans}")
        i += 1
        cashed.clear()

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 12\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 7251 copied -_-
    # Part 2
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()