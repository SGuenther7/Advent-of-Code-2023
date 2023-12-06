
# 0 98 2
# 2 50 48

# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

# Seed number 79 corresponds to soil number 81.
# Seed number 14 corresponds to soil number 14.
# Seed number 55 corresponds to soil number 57.
# Seed number 13 corresponds to soil number 13.

# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

class Seed:
    def __init__(self, id):
        self.id = id
        self.soil = -1
        self.fertilizer = -1
        self.water = -1
        self.light = -1
        self.temp = -1
        self.humi = -1
        self.loc = -1
    def __str__(self):  
        return "<" + str(self.id) + "," + str(self.soil) + "," + str(self.fertilizer) + "," + str(self.water) + "," \
            + str(self.light) + ","+ str(self.temp) + "," + str(self.humi) + "," + str(self.loc) + ">"
    def __repr__(self):  
        return str(self)
    
testData = [
    "seeds: 79 14 55 13",
    "\n",
    "seed-to-soil map:",
    "50 98 2",
    "52 50 48",
    "\n",
    "soil-to-fertilizer map:",
    "0 15 37",
    "37 52 2",
    "39 0 15",
    "\n",
    "fertilizer-to-water map:",
    "49 53 8",
    "0 11 42",
    "42 0 7",
    "57 7 4",
    "\n",
    "water-to-light map:",
    "88 18 7",
    "18 25 70",
    "\n",
    "light-to-temperature map:",
    "45 77 23",
    "81 45 19",
    "68 64 13",
    "\n",
    "temperature-to-humidity map:",
    "0 69 1",
    "1 0 69",
    "\n",
    "humidity-to-location map:",
    "60 56 37",
    "56 93 4",
]

from enum import Enum
class Part(Enum):
    Seed_to_soil = 0
    Soil_to_fertilizer = 1
    Fertilizer_to_water = 2
    Water_to_light = 3
    Light_to_temp = 4
    Temp_to_humi = 5
    Humi_to_loc = 6

seeds = []
parts = []
hashed_seeds = {}

def calc_Seed_loc(seed):

    ret = seed
    for table in parts:
        
        search = ret
        
        for (dest, src, step) in table:
        #f search == 77:
        #   print(str(table) + " | " + str(dest) + " " + str(src) + " " + str(step) + " | " + str(search))

            if src <= search < src + step:
                ret = search + dest - src
                #print(ret)
                break

    return ret


import datetime
import time


def merge_ranges(rangeA : (), rangeB: ()):
    return (rangeA[0], rangeB[1])

def test_intersection(rangeA, rangeB):

    [a,b] = sorted([rangeA,rangeB])

    return (a[1] >= b[0])

def merge_all(ranges : [()]):

    ranges = sorted(ranges)

    merged = [ranges.pop(0)]

    for r in ranges:
        if test_intersection(merged[-1], r):
            merged.append( merge_ranges( merged.pop(), r ) )
        else:
            merged.append(r)

    return merged

def apply_filter(filters : [], ranges : [()]) -> [()]:
    ret = []
    to_scan = ranges

    while to_scan:
        #print(f"filter: {filters}")
    #    print(f"to_scan: {to_scan}")
        # after all filters
        if to_scan[0][0] > (filters[-1][0] + filters[-1][2] - 1):
       #     print("after")
            ret.append(to_scan.pop(0))
            continue

        for (src, dest, step) in filters:

            if len(to_scan) <= 0:
                break
            # before all filters
            if to_scan[0][0] < src :
                start = to_scan[0][0]
                end = min(to_scan[0][1], src )

                ret.append((start, end))
                if (end - start) < (to_scan[0][1] - to_scan[0][0]):
                    to_scan[0] = (src, to_scan[0][1])
                else:
                    to_scan.pop(0)
                    break
            
            if test_intersection(to_scan[0], (src, src + step - 1)):
                ra = to_scan[0]

            #    print(f"found Filter {(src,dest,step)} for {ra}")
                start = max(src, ra[0])
                end = min(src + step - 1, ra[1])
                
                length =  end - start
                off = dest - src
           #     print(f"-- {start} {end} {length}")
                new_Tuple = (start + off, end + off)
                ret.append(new_Tuple)
           #     print(f"-- {new_Tuple}")

                if length == ra[1] - ra[0]:
                    r = to_scan.pop(0)
                    #print(f"r: {r}")
                 #   print("no rest")
                    break
                else :
                  #  print("rest")

                    start_new = to_scan[0][0] + length + 1
                    end_new = to_scan[0][1]
                    if start_new == end_new:
                    #    print(f"one Number")
                        ret.append((start_new + off, end_new + off))
                        to_scan.pop(0)
                    else:
                        to_scan[0] = (start_new, end_new)
                    break
            
        #time.sleep(0.5)
                
    return ret

    #for filter in filters:


def extract_seeds(seeds):

    (_,seeds) = seeds.split(": ")
    seeds = seeds.split(" ")

  #  print(f"seeds: {seeds}")
    ranges = []
    while seeds:
        start = int(seeds.pop(0))
        end = start + int(seeds.pop(0))
        ranges.append((start, end)) # TODO
        
        #ranges.append((start, start)) # TODO
        #ranges.append((end - start, end - start)) # TODO

   

    #print(ranges)
    ranges = merge_all(ranges)
  #  print(f" ex seed ranges: {ranges}")

    for filter in parts:
      # print("____________________________________________________")
      # print(f" ex used filter: {filter}")
        ranges = apply_filter(filter, ranges)
        ranges = merge_all(ranges)

       # print(f" ex merged ranges: {ranges}")

  # print("__________________")
  # print(f" ex seed ranges: {ranges}")
    return ranges[0][0]

def doIt(data):

    seeds = data.pop(0)
    data.pop(0)

    for i in range(7):
        part = []

        while len(data) > 0:
            if data[0] != "\n":
                part.append(data.pop(0))
            else: 
                data.pop(0)
                break

        lines = []
        part.pop(0)

        for elem in part:
            dest, src, step = elem.split(" ")
            dest = int(dest)
            src = int(src)
            step = int(step)
        
            lines.append([ src, dest, step])
        lines = sorted(lines)
        
        #print(lines)
        parts.append(lines)

    #for part in parts:
     #   print(part)

    lowest = extract_seeds(seeds)
        
    return lowest

from time import process_time


def main():
    print(f"Start: {(datetime.timedelta( seconds=( process_time() ) ) )}")
    file = open("..\Python\Advent of Code 2023\Day 5\Day_5-1_input.txt", 'r')

    data = file.readlines() 
    #data = testData
    
    t = process_time()

    num = doIt(data)

    elapsed_time = process_time() - t

    print("----")
    print(num)
    # instant
    # 28580589
    
    print(elapsed_time)

if __name__ == "__main__":
    main()