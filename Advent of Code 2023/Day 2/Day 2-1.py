

testData = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def is_game_possible(line):

    dat = line.split(": ")
    gameID = int(dat[0].split(" ")[1])
    sets = dat[1].split("; ")
    test = True

    for set in sets:
        test = test and True and is_set_possible(set)

    if test:
        return gameID
    else:
        return 0

def is_set_possible(set):
    
    cat = set.split(", ")
    test = True
    for c in cat:
       dat = c.split(" ")
       test = test and True and is_play_possible(int(dat[0]), dat[1])  

    return test

def is_play_possible(num, col):

    if col.startswith("red") and num > 12:
        return False
    if col.startswith("green") and num > 13:
        return False
    if col.startswith("blue") and num > 14:
        return False
    return True

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