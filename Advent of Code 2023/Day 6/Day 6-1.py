testData = [
    "Time:      7  15   30",
    "Distance:  9  40  200",
]

import re

def get_n_ways_to_win( time, dist ):
    ways_to_win = 0
    #print("_______")
    for waited in range(time):
        driven = waited * (time - waited)
      #  print(f" - {waited} {driven} {dist} {time}")
        if driven > dist:
       #     print("win")
            ways_to_win += 1

    return ways_to_win

def doIt(data):

    time_dist = []
    #print(data)
    _, times = data[0].split(": ")
    _, dist = data[1].split(": ")

    times = re.findall(r'\d+', times)
    dist = re.findall(r'\d+', dist)

    while times and dist:
        #print(f"{times[0]} {dist[0]}")
        time_dist.append((times.pop(0), dist.pop(0)))

    ways_to_win = []
    for ( time, dist ) in time_dist:
        ret = get_n_ways_to_win(int(time), int(dist))
        #print(ret)
        ways_to_win.append(ret)

    ret = 1
    for way in ways_to_win:
       # print(way)
        ret *= way

    return ret

def main():

    file = open("..\Python\Advent of Code 2023\Day 6\Day_6-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    
    nums = doIt(data)

    accum = 0

    #for num in nums:
   #     accum += num

    print("----")
    print(nums)

if __name__ == "__main__":
    main()