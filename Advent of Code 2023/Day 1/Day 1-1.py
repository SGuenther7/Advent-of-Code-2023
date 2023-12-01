
# lines of Text
# first and last Digit -> 2 digit number
# answer = every lines number added

# 1abc2         -> 12
# pqr3stu8vwx   -> 38
# a1b2c3d4e5f   -> 15
# treb7uchet    -> 77
#             |=> 142

# import numpy

testData = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet" 
] 

def get_answer(input):

    accum = 0
    for line in input:
        digits = list(filter(str.isdigit, line))
        num = int(digits[0]) * 10 + int(digits[-1])        
        accum += num

    return accum
    #return numpy.cumsum(numbers)[-1]

def main():

    file = open("..\Python\Advent of Code 2023\Day 1\day_1-1_input.txt", 'r')

    data = file.readlines()
    #data = testData
    
    answer = get_answer(data)
    
    print(answer)

if __name__ == "__main__":
    main()