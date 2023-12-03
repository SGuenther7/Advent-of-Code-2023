
import re

testData = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
".............................................................................................................................................",
"......=.........................=........733..433...128..............*.......889...........................661.........-358...$....281......",
".....35..........$...........834.../699...../.-......................461.......-........*...................*..................374....=.#412",
"............763..201..$............................392........341........96......723.340.........327.736...1..$897.....471..................",
".....*512..*.........221.............125$....257.....@.....................*.277.*................*...*................................@....",

".....205...572................696........&.....@.....@............709..611.............=.......270........*....165......783.......790.......",
"......................965.........709..826....................882*......%..775.........391....*......985.5........*179.....*47.......&......",
".....451............@................#..................804..................$..161...........837..............*................$904....176.]",
]

# Classes

class Num:
    def __init__(self, val, start, end):
        self.val = val
        self.start = start
        self.end = end
    def __str__(self):  
        return f"<{self.val}:{self.start},{self.end}>" 
        #return f"{self.val}_{self.c}" 
    def __repr__(self) -> str:
        return str(self)

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):  
        return f"({self.x},{self.y})"  
    def __repr__(self) -> str:
        return str(self)

# Logic

def is_Num_next_to_Symbol(num, text):

    x1 = num.start.x - 1 
    y1 = num.start.y - 1
    x2 = num.end.x + 1 
    y2 = num.end.y + 1 

    if x1 < 0 : x1 = 0
    if y1 < 0 : y1 = 0

    if y2 >= len(text) : y2 = len(text) - 1
    if x2 >= len(text[y2]) : x2 = len(text[y2]) - 1

    start = Vec(x1, y1)
    end = Vec(x2, y2)

    for x in range(end.x - start.x + 1):
        for y in range(end.y - start.y + 1):

            char = text[y + start.y][x + start.x]

            if not char.isdigit() and char != '.' and char != '\n':
                return True, char

    return False," "

def extract_Nums(line, y):

    nums = []
    lastOff = 0

    for num in re.findall(r'\d+',line):
        off = line.find(num, lastOff)
        start = Vec(off, y)
        end = Vec(off + len(num) - 1, y)
        val = Num(int(num), start, end)
        
        nums.append(val)
        lastOff = off + len(num)
    
    return nums

def get_numbers_Next_to_Symbol(data):
    
    nums = []

    for i in range(len(data)):
        vals = extract_Nums(data[i], i)

        # empty == false
        if vals:
            nums += vals
    
    ret = []
    for num in nums:
        t, c = is_Num_next_to_Symbol(num, data)
        if t:
            num.c = c
            ret.append(num)
    return ret

# Start

def main():

    file = open("..\Python\Advent of Code 2023\Day 3\Day_3-1_input.txt", 'r')
    data = file.readlines() 
    nums = get_numbers_Next_to_Symbol(data)
    
    accum = 0

    for num in nums:
        accum += num.val

    print("----")
    print(accum)

if __name__ == "__main__":
    main()
