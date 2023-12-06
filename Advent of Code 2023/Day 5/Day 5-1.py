
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
    Seeds = 0
    Seed_to_soil = 1
    Soil_to_fertilizer = 2
    Fertilizer_to_water = 3
    Water_to_light = 4
    Light_to_temp = 5
    Temp_to_humi = 6
    Humi_to_loc = 7

#lookUp = {}

def get_lookUp(table, search):
    
    ret = search
    #print("________________________________________________")

    for line in table:
        dest, src, step = line.split(" ")
        dest = int(dest)
        src = int(src)
        step = int(step)
        off = dest - src
        
        #print(str(search) + " " + str(src) + " " + str(dest)+ " " + str(off))
        if src <= search and (src + step) >= search:
            ret = search + off
            #print("FOUND: " + str(ret))
            break

    #print(ret)
    return ret

def get_lookUp2(table, search):

    look = {}

    for line in table:
        dest, src, step = line.split(" ")
        dest = int(dest)
        src = int(src)
        step = int(step)
        
        #print(src)
        #print(dest)
        #print(step)
        for i in range(step):
            look[src + i] = dest + i

    ret = look.get(search, search)
    return ret
    #lookUp[part] = look

parts = []

def calc_Seed(seed):
    #print("_____________")
    #print(Part.Seed_to_soil.value)
   # print(parts)
    seed.soil       = get_lookUp(parts[Part.Seed_to_soil.value],        seed.id)
    seed.fertilizer = get_lookUp(parts[Part.Soil_to_fertilizer.value],  seed.soil)
    seed.water      = get_lookUp(parts[Part.Fertilizer_to_water.value], seed.fertilizer)
    seed.light      = get_lookUp(parts[Part.Water_to_light.value],      seed.water)
    seed.temp       = get_lookUp(parts[Part.Light_to_temp.value],       seed.light)
    seed.humi       = get_lookUp(parts[Part.Temp_to_humi.value],        seed.temp)
    seed.loc        = get_lookUp(parts[Part.Humi_to_loc.value],         seed.humi)
    
    #print(seed)
    return seed
          
#def calc_lookUp(data):
#    get_lookUp(Part.Seed_to_soil.value, data[Part.Seed_to_soil.value])
#    get_lookUp(Part.Soil_to_fertilizer.value, data[Part.Soil_to_fertilizer.value])
#    get_lookUp(Part..value, data[Part.Fertilizer_to_water.value])
#    get_lookUp(Part..value, data[Part.Water_to_light.value])
#    get_lookUp(Part..value, data[Part.Light_to_temp.value])
#    get_lookUp(Part..value, data[Part.Temp_to_humi.value])
#    get_lookUp(Part..value, data[Part.Humi_to_loc.value])
        
def extract_seeds(line):
    #print(type(line))
    #print(type("strdsrsf"))
    #print(line)

    _, seeds = line.split(": ")
    seeds = seeds.split(" ")
    
    seed_list = []
    for seed in seeds:
        seed_list.append(Seed(int(seed)))
    
    #print(seed_list)
    return seed_list

def doIt(data):

    #parts = []

    for i in range(8):
        part = []
        while len(data) > 0:
            if data[0] != "\n":
                # print(data[0])
                part.append(data.pop(0))
            else: 
                data.pop(0)
                break
        parts.append(part)

    #for line in parts:
    #    print(line)

    #print("____________")

    parts[Part.Seed_to_soil.value].pop(0)
    parts[Part.Soil_to_fertilizer.value].pop(0)
    parts[Part.Fertilizer_to_water.value].pop(0)
    parts[Part.Water_to_light.value].pop(0)
    parts[Part.Light_to_temp.value].pop(0)
    parts[Part.Temp_to_humi.value].pop(0)
    parts[Part.Humi_to_loc.value].pop(0)

    #for line in parts:
    #    print(line)

    #calc_lookUp(parts)
    seeds = extract_seeds(parts[Part.Seeds.value][0])
    #seeds[0].soil = src_to_dest(seeds[0], parts[Part.Seed_to_soil.value])
    
    print(len(seeds))

    for seed in seeds:
        seed = calc_Seed(seed)
        #seed.soil = lookUp[Part.Seed_to_soil.value]\
        #    .get(seed.id, seed.id)
        #seed.fertilizer = lookUp[Part.Soil_to_fertilizer.value]\
        #    .get(seed.soil, seed.soil)
        #seed.water = lookUp[Part.Fertilizer_to_water.value]\
        #    .get(seed.fertilizer, seed.fertilizer)
        #seed.light = lookUp[Part.Water_to_light.value]\
        #    .get(seed.water, seed.water)
        #seed.temp = lookUp[Part.Light_to_temp.value]\
        #    .get(seed.light, seed.light)
        #seed.humi = lookUp[Part.Temp_to_humi.value]\
        #    .get(seed.temp, seed.temp)
        #seed.loc = lookUp[Part.Humi_to_loc.value]\
        #    .get(seed.humi, seed.humi)

    #print("___________")
    lowest = 1_000_000_000
    for seed in seeds:
        #print(seed)
        if lowest > seed.loc:
            lowest = seed.loc
    
    return lowest

from time import process_time_ns


def main():

    file = open("..\Python\Advent of Code 2023\Day 5\Day_5-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    
    t = process_time_ns()

    num = doIt(data)

    elapsed_time = process_time_ns() - t
    # part1 | 240320250
    # part2 | 28580590
    print("----")
    print(num)
    print(elapsed_time)

if __name__ == "__main__":
    main()