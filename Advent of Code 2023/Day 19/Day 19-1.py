testData = [
    "px{a<2006:qkq,m>2090:A,rfg}\n",
    "pv{a>1716:R,A}\n",
    "lnx{m>1548:A,A}\n",
    "rfg{s<537:gd,x>2440:R,A}\n",
    "qs{s>3448:A,lnx}\n",
    "qkq{x<1416:A,crn}\n",
    "crn{x>2662:A,R}\n",
    "in{s<1351:px,qqz}\n",
    "qqz{s>2770:qs,m<1801:hdj,R}\n",
    "gd{a>3333:R,R}\n",
    "hdj{m>838:A,pv}\n",
    "\n",
    "{x=787,m=2655,a=1222,s=2876}\n",
    "{x=1679,m=44,a=2067,s=496}\n",
    "{x=2036,m=264,a=79,s=2244}\n",
    "{x=2461,m=1339,a=466,s=291}\n",
    "{x=2127,m=1623,a=2188,s=1013}\n",
]

class Part:
    def __init__(self, values):
        self.vals = values
    def __repr__(self) -> str:
        return f"{[ self.vals[c] for c in self.vals.keys()]}"
    def getRating(self):
        return sum([ self.vals[c] for c in self.vals.keys()])


def evalParts(parts):
    accepted = []

    for part in parts:
        #print(f"--- \t {part}")
        curWF = "in"
        processed = False
        while not processed:
            if curWF == "A":
                accepted.append(part)
                processed = True
                break
            elif curWF == "R":
                processed = True
                break
            exp = workFlows[curWF]
            
            for rule in exp:
               # print(f" - {rule}")
                if rule != exp[-1]:
                    r, t = rule
                    x = r[0]
                    #print(x)
                    x = part.vals[x]
                    ex = str(x) + r[1:]
                   # print(f"{ex} -> {eval(ex)}")
                    if eval(ex):
                        curWF = t
                        break
                else:
                    if rule == "A":
                        accepted.append(part)
                        processed = True
                    elif rule == "R":
                        processed = True
                    else:
                        curWF = rule
                    break

    #print("Parts:")
    #for part in accepted:
    #    print(part)
    return sum([part.getRating() for part in accepted])

workFlows = {}
def doIt(data : [str]) -> int:
    
    parts = []

    while data:
        line = data.pop(0)
        if line == "\n":
            break
        line = line.strip()
        wf, rest = line.split("{")
        r = rest[:-1].split(",")
        rules = []
        for rule in r:
            if ":" in rule:
                exp, target = rule.split(":")
                rules.append((exp,target))
            else:
                rules.append(rule)

        #print(f"{wf} : {rules}")

        workFlows[wf] = rules

    print("------------")
    while data:
        line = data.pop(0).strip()
        vals = line[1:-1].split(",")

        values = {}

        for v in vals:
            c, num = v.split("=")
            values[c] = int(num)
        #print(values)
        parts.append(Part(values))

    #print(workFlows)
    #print(parts)
    ans = 0
    ans = evalParts(parts)

    return ans    

from time import process_time, sleep
import datetime

def main():

    file = open("..\Python\Advent of Code 2023\Day 19\input.txt", 'r')

    data = file.readlines() 
    #data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 263_678 First Try
    # Part 2
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()