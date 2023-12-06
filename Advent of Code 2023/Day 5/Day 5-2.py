
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

#def get_lookUp(table, search):
#    
#    ret = search
#
#    for (dest, src, step) in table:
#        #f search == 77:
#        #   print(str(table) + " | " + str(dest) + " " + str(src) + " " + str(step) + " | " + str(search))
#
#        if src <= search <= src + step:
#            ret = search + dest - src
#            #print(ret)
#            break
#
#    return ret

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


#def calc_Seed_loc(seed, count):
#
#    ret = seed
#    rest = count
#
#    min_len = 0
#
#    for table in parts:
#        
#        search = ret
#
#        min_len_round = 1
#        
#        for (dest, src, step) in table:
#        #f search == 77:
#        #   print(str(table) + " | " + str(dest) + " " + str(src) + " " + str(step) + " | " + str(search))
#
#            if src <= search <= src + step:
#               ret = search + dest - src
#               
#               min_len_round = (dest + step) - ret 
#               #print(ret)
#
#                break
#        if min_len == 0 or min_len > min_len_round:
#            min_len = min_len_round
#
#       # print(f"{ret} {src} {step} {min_len_round} {min_len}")
#    #for (dest, src, step) in parts[0]:
#    #    if src <= ret <= (src + step):
#    #        c = (src + step) - ret
#    #        print(f"{ret} {src} {step} : {c} | {count}")
#    #        
#
#    #if src <= search <= src + step:
#           #ret = search + dest - src
#            #print(ret)
#    
#    return (ret, rest-min_len, min_len)

from threading import Thread
import multiprocessing as m

class NewThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
        Thread.__init__(self, group, target, name, args, kwargs)

    def run(self):
        if self._target != None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self, *args):
        Thread.join(self, *args)
        return self._return

def extract_seeds(line):

    _, seeds = line.split(": ")
    seeds = seeds.split(" ")
    
    seed_list = []

    #print(seeds)

    nearest_loc = 100_000_000_000
    
    t = process_time()

    locs = []
    i = 0
    processes = []

    pool = m.Pool(processes=10)

    while seeds:
        id = int(seeds.pop(0))
        count = int(seeds.pop(0))
        #count = 1
        #proc = m.Process(target = calcNearest, args=(id, count, i))
        #proc.start()
        #processes.append(proc)
        #if (i == 3 or i == 4 or i == 5 or i == 8 or i == 9):
        proc = pool.apply_async(func = calcNearest, args = (id, count, parts, i))
        processes.append(proc)
    
        i += 1
        #loc = calcNearest(id, count)
        #if nearest_loc > loc : 
        #    nearest_loc = loc
        
    pool.close()

    i = 0
    for proc in processes:
        #proc.join()
        loc = proc.get() 
        print(f"=> {i} : {loc}")
        locs.append(loc)
        i += 1


    print(locs)
        
    elapsed_time = process_time() - t
    print("elapsed: "+ str(elapsed_time)) 
    #print(locs)

    #nearest_loc = min(locs)

    return min(locs)

import datetime
import time

def calcNearest(seed_start, count, parts, thread_ID = 0,):
    t = process_time()
    #nearest_loc = 100_000_000_000  
    
    nearest_loc = 100_000_000_000  

    update = 10_000_000
    i = 0
    min_len_round = 1
    
    def calc_Seed_loc(seed):

        ret = seed
        for table in parts:    
            search = ret   
            for (dest, src, step) in table:
                if src <= search <= src + step:
                    ret = search + dest - src
                    break
            #print(f"- {ret}")

        return ret
    
    for i in range(count):
    #while count > 0:
        if (i % update) == 0:    
            elapsed_time = process_time() - t
            remaining = count - i
            print(f"Thread {thread_ID} = {elapsed_time} \t| tested {(i/count) * 100.0} % | \t{i} of {count} | remaining {remaining} | {(datetime.timedelta(seconds=(elapsed_time * (remaining / update))))} | {min_len_round}")
            t = process_time()

        loc = calc_Seed_loc(seed_start + i)
        #id = seed_start + i
        #loc = hashed_seeds.get(id, calc_Seed_loc(id))
        #hashed_seeds[id] = loc
       # print(loc)
        
        #(loc, rest, min_len) = calc_Seed_loc(id, count)
        #count = rest
        #min_len_round = min_len
        #time.sleep(1)
        #print(loc)

        if loc < nearest_loc:
            nearest_loc = loc

        i += 1
    #print(nearest_loc)

    return nearest_loc

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
        
            lines.append([dest, src, step])
        
        #print(lines)
        parts.append(lines)

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
    #nums = [28580590, 50952572, 240320250, 1000000000, 1000000000, 1000000000, 816145253, 414542692, 1000000000, 1000000000]
    #        0          1         2            3          4          5              6         7          8           9
    
    #nums = [28580590, 50952572, 240320250, 1211805271, 3870371252, 1000000000, 816145253, 414542692, 1000000000, 1000000000]

    # [28580590, 50952572, 240320250, 1211805271, 3870371252, 1451868056, 816145253, 414542692, 1986294484, 1070939631]
    # 28580590
     
     #num = min(nums)
    # 28580590 hat <110 min gedauert -_-
    print("----")
    print(num)
    
    print(elapsed_time)

if __name__ == "__main__":
    main()