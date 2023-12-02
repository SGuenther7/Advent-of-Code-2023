

testData = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def is_game_possible(line):

    dat = line.split(": ")
    sets = dat[1].split("; ")
    max = Max(0,0,0)

    for set in sets:
        max = is_set_possible(set, max)

    return max.red * max.green * max.blue

def is_set_possible(set, max):
    
    cat = set.split(", ")

    for c in cat:
       dat = c.split(" ")
       max = getMax(int(dat[0]), dat[1], max)  
    
    return max

class Max:
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
    def __str__(self):  
        return "(" + str(self.red) + "," + str(self.green) + "," + str(self.blue) + ")"  

def getMax(num, col, currentMax: Max):

    if col.startswith("red") and num > currentMax.red:
        return Max(num, currentMax.green, currentMax.blue)
    if col.startswith("green") and num > currentMax.green:
        return Max(currentMax.red, num, currentMax.blue)
    if col.startswith("blue") and num > currentMax.blue:
        return Max(currentMax.red, currentMax.green, num)
    return currentMax

def main():

    file = open("..\Python\Advent of Code 2023\Day 2\Day_2-1_input.txt", 'r')

    data = file.readlines()
    #data = testData

    num = 0
    for game in data:
        num += is_game_possible(game)

    print("Answer: " + str(num))

if __name__ == "__main__":
    main()