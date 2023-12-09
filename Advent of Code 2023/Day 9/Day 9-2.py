testData = [
    "0 3 6 9 12 15", # 18
    "1 3 6 10 15 21", # 28
    "10 13 16 21 30 45", # 68
]
# 114

def getNextNum(nums : [int]):
    diff = []

    for i in range(len(nums) - 1):
        diff.append(nums[i + 1] - nums[i])

    print(f"{diff} | {nums} | ")

    if all( val == 0 for val in diff ):
        print(f"--zero {diff}")
        return nums[0]
    else:
        #next = getNextNum(diff)
        print(f"-- calc |{nums[0]} | {diff}")
        return nums[0] - getNextNum(diff)

    # 1_669_088_736 too High
    # 1_666_171_625 too Low
    

def doIt(data):
    rows = []
    for line in data:
        numbers = [int(num) for num in line.strip().split(" ")]
        rows.append(numbers)

    accum = 0
    next_vals = []
    for nums in rows:
        next = getNextNum(nums)
        next_vals.append(next)
        accum += next
        print("_______")
        #print(nums)

    print(next_vals)
    return accum    

from time import process_time
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 9\Day_9-1_input.txt", 'r')

    data = file.readlines() 
    #data = testData

    t = process_time()
    print(datetime.datetime.now())    

    answer = doIt(data)

    print("----")
    print(answer)

    # 1_669_088_736 too High
    # 1_666_171_625 too Low
    
    # 1_666_172_641 correct

    # part2
    # 933
    elapsed_time = process_time() - t
    print(f"Start: {(datetime.timedelta( seconds=( elapsed_time ) ) )}")

if __name__ == "__main__":
    main()