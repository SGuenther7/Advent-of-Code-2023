testData = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
]

import re

def getRoundPoints(round):
    points = 0
    _, numbers = round.split(": ")
    winning, drawn = numbers.split("|")
 
    winning = set(re.findall(r'\d+',winning))
    drawn = set(re.findall(r'\d+', drawn))

    for num in winning:
        if num in drawn:
            points += 1

    return points


def doIt(data):
    cards = 0
    modif = {}

    for i in range(len(data)):
        modif[ i ] = 1

    index = 0
    for round in data:

        cards_per_round = getRoundPoints(round)
        won_cards =  modif[index]

        for i in range(cards_per_round):
            modif[i + 1 + index] += modif[index]

        cards += won_cards
        index += 1

    return cards

def main():

    file = open("..\Python\Advent of Code 2023\Day 4\Day_4-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    
    points = doIt(data)

    print("----")
    print(points)

if __name__ == "__main__":
    main()