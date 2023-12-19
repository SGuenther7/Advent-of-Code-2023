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

acceptedRanges = {}

class Part:
    def __init__(self):
        self.vals = { "x":(1,4000), "m":(1,4000), "a":(1,4000), "s":(1,4000) }
        self.applied = []
                
    def __repr__(self):
        
        #'{:3d}'.format(99)
        #return f"{self.vals}\t= {self.applied}"

        x_min, x_max = self.vals["x"]
        m_min, m_max = self.vals["m"]
        a_min, a_max = self.vals["a"]
        s_min, s_max = self.vals["s"]
        
        x_min = '{:5d}'.format(x_min)
        x_max = '{:5d}'.format(x_max)
        m_min = '{:5d}'.format(m_min)
        m_max = '{:5d}'.format(m_max)
        a_min = '{:5d}'.format(a_min)
        a_max = '{:5d}'.format(a_max)
        s_min = '{:5d}'.format(s_min)
        s_max = '{:5d}'.format(s_max)

        return "{" + f"x:({x_min},{x_max}), ({m_min},{m_max}), ({a_min},{a_max}), ({s_min},{s_max}) -> {self.applied}"

    def getCount(self) -> int:
        x_min, x_max = self.vals["x"]
        m_min, m_max = self.vals["m"]
        a_min, a_max = self.vals["a"]
        s_min, s_max = self.vals["s"]
        count = (x_max - x_min + 1) * (m_max - m_min + 1) * (a_max - a_min + 1) * (s_max - s_min + 1) 
        return count

    def count(self) -> int:
        count = self.getCount() 
        
        #print(f"--counted {count}")
        #print(self)

        parts = acceptedRanges.get(0, [])
        parts.append(self)
        acceptedRanges[0] = parts
        return count

    def applyRule(self, wf, depth = 0) -> int:
        
        self.applied.append(wf)
        indent = "".join(["-" for i in range(depth)])

        if wf == "A":
            print(f"{self}")
            return self.count()
        elif wf == "R":
            return 0
        
        rules = workFlows[wf]
        #print(f"|{indent} {wf} {rules}")
        count = 0

        for rule in rules:
            #print(f"{rule} | {self.applied}")

            if ":" in rule:
                rest, target = rule.split(":")
                c = rest[0]
                s = rest[1]
                v = int(rest[2:])
                
                #print(f"|{indent}-> {c} {s} {v} -> {target}")

                other = copy.deepcopy(self)
                min, max = self.vals[c]
                ifTrue, ifFalse = applySign(s, min, max, v)
                
                self.vals[c] = ifFalse
                other.vals[c] = ifTrue

                #count += temp.applyRule(target, depth + 1)
                other.applyRule(target, depth + 1)

                #temp = copy.deepcopy(self)
                #min,max = temp.vals[c]
                #min, max = applySign(s, min, max, v)
                #temp.vals[c] = (min, max)
                ##count += temp.applyRule(target, depth + 1)
                #temp.applyRule(target, depth + 1)
            else:
                #count += self.applyRule(rule, depth + 1)
                self.applyRule(rule, depth + 1)
    
def applySign(s, min, max, val):
    new_min = min
    new_max = max

    if s == ">":
        return ((val + 1 , max), (min, val))
    elif s == "<":
        return ((min, val - 1), (val, max) )
    
workFlows = {}
def doIt(data : [str]) -> int:
    
    while data:
        line = data.pop(0)
        
        if line == "\n":
            break

        line = line.strip()
        wf, rest = line.split("{")
        r = rest[:-1].split(",")
        #rules = []
        #for rule in r:
            #if ":" in rule:
            #    exp, target = rule.split(":")
            #    rules.append((exp,target))
            #else:
            #    rules.append(rule)

        #print(f"{wf} : {rules}")

        #workFlows[wf] = rules
        workFlows[wf] = r

    print("------------")
    
    ans = 0
    
    part = Part()
    print(part.applyRule("in"))
    print("-----")

    #print(f"|{acceptedRanges}|")
    count = 0
    iter = 0
    for part in acceptedRanges[0]:
        iter += 1
        count += part.getCount()
        print(f"{iter} -> {part}")

    print(f"counted: {count}")

    # counted 495709756631235
    #         167409079868000
    # should  167409079868000
    # max     256000000000000

    partA = Part()
    partA.vals["m"] = (1,2)
    partB = copy.deepcopy(partA)
    partB.vals["x"] = (1,2)

    print(partA)
    print(partB)

    return count    

from time import process_time, sleep
import datetime
import copy

def main():

    file = open("..\Python\Advent of Code 2023\Day 19\input.txt", 'r')

    data = file.readlines() 
   # data = testData

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(answer)
    print("\n-------")

    # Part 1
    # 263_678 First Try
    # Part 2
    # 125455345557345 First Try
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()