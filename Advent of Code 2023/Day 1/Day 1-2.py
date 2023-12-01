# same as day 1-1
# but digits can be spelled out
# one, two, three, four, five, six, seven, eight, and nine

# two1nine          -> 29
# eightwothree      -> 83
# abcone2threexyz   -> 13
# xtwone3four       -> 24
# 4nineeightseven2  -> 42
# zoneight234       -> 14
# 7pqrstsixteen     -> 76
#                 |=> 281

# import numpy

testData = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen"
] 

alphaNums = [ ["one", 1], ["two", 2], ["three", 3], ["four", 4], ["five", 5], ["six", 6], ["seven", 7], ["eight", 8], ["nine", 9] ]

def get_answer(input : str):

    accum = 0
    for line in input:
        #print(line)
        digits = getDigit(line)
       # print(digits)
        num = (digits[0]) * 10 + (digits[-1])        
        accum += num
        #print(num)
    return accum
    #return numpy.cumsum(numbers)[-1]

def getDigit(line : str):
    digits = []

    if len(line) > 0:
        if line[0].isdigit():
            #print("found digit: " + line[0])
            digits.append(int(line[0]))
            digits += getDigit(line[1:])

        else:
            for alpha in alphaNums:
                if line.startswith(alpha[0]):
                    #print("found: " + alpha[0] + " " + str(alpha[1]))
                    digits.append(alpha[1])
                    digits += getDigit(line[len(alpha[0]):])
                    break
            digits += getDigit(line[1:])

    return digits
            
def main():

    file = open("..\Python\Advent of Code 2023\Day 1\day_1-2_input.txt", 'r')

    data = file.readlines()
    #data = testData
    
    answer = get_answer(data)

    print(answer)

if __name__ == "__main__":
    main()