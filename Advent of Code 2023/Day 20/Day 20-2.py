from enum import Enum

testData = [
    "broadcaster -> a, b, c\n",
    "%a -> b\n",
    "%b -> c\n",
    "%c -> inv\n",
    "&inv -> a\n",
]

testData2 = [
    "broadcaster -> a\n",
    "%a -> inv, con\n",
    "&inv -> b\n",
    "%b -> con\n",
    "&con -> output\n",
]

class Pulse(Enum):
    LOW = 0
    HIGH = 1

class Modul:
    def __init__(self, type, name, outputs):
        self.type = type
        self.name = name
        self.outputs = outputs
        self.receivedPulses = []
        self.sendHigh = 0
        self.sendLow = 0
        self.signalReceivedThisCycle = False

        self.flipFlopOn = False
        self.conMemory = {}

    def __repr__(self) -> str:
        return f"{self.name}({self.type}):\tout:{self.outputs}\t| {self.receivedPulses}\t| {self.conMemory if self.type == "&" else ""}"

    def pressButton(self):
        if self.name == "button":
            modules["broadcaster"].receivePulse(Pulse.LOW, self.name)
            self.sendLow += 1
            modules["broadcaster"].signalReceivedThisCycle = False

    def getSentSignals(self) -> (int,int):
        return (self.sendHigh, self.sendLow)

    def processPulse(self, presses = -1) -> None:
        #print(f"-- {self.name} {self.receivedPulses}")

        if not self.signalReceivedThisCycle and len(self.receivedPulses) > 0:
            if self.type == "broadcaster":
                ret = self.broadcasterProcess(presses)            
            elif self.type == "%":
                ret = self.flipFlopProcess(presses)
            elif self.type == "&":
                ret = self.conjunctionProcess(presses)
            else:
                print(f"ERROR {self.type}")
            self.receivedPulses.pop(0)
            return ret
        
    def broadcasterProcess(self, presses = -2):
        return self.sendPulses(self.receivedPulses[0], presses)
    
    def flipFlopProcess(self, presses = -3):
        if self.receivedPulses[0] == Pulse.HIGH:
            return
        if self.flipFlopOn:
            ret = self.sendPulses(Pulse.LOW, presses)
            self.flipFlopOn = False
            return ret 
        elif not self.flipFlopOn:
            ret = self.sendPulses(Pulse.HIGH, presses)
            self.flipFlopOn = True
            return ret
        
    def conjunctionProcess(self, presses = -4):
        #print(self.conMemory.values())
        t = all( self.conMemory[pulse] == Pulse.HIGH for pulse in self.conMemory)
        pulse = Pulse.LOW if t else Pulse.HIGH
        return self.sendPulses(pulse, presses)

    def sendPulses(self, pulse, presses = -5):
        ret = None
        if self.name in ptBefore:# and pulse == Pulse.HIGH:
            #print(f"Pulse {pulse.name} {self.name} {ptBefore} {ptBefore[self.name]}")
            if ptBefore[self.name] == None and pulse == Pulse.HIGH:
                print(f"-- {self.name} {presses}")
                ptBefore[self.name] = presses


        for recipient in self.outputs:
            #print(f"{self.name} -{pulse.name}-> {recipient}")
            if recipient in modules:
                modules[recipient].receivePulse(pulse, self.name)
            elif recipient == "rx" and pulse == Pulse.LOW:
                ret = "rx"
            
            if pulse == Pulse.HIGH:
                self.sendHigh += 1
            elif pulse == Pulse.LOW:
                self.sendLow += 1
            
        return ret
    
    def receivePulse(self, pulse : Pulse, senderName) -> None:
        if self.type == "&":
            self.conMemory[senderName] = pulse
        if len(self.receivedPulses) == 0:
            self.signalReceivedThisCycle = True
        self.receivedPulses.append(pulse)

modules = {}
ptBefore = {}

def doIt(data : [str]) -> int:

    hi_before = 0
    lo_before = 0        
    hi_all = 0
    lo_all = 0

    for line in data:
        #print(line.strip())
        start, outputs = line.strip().split(" -> ")
        outputs = outputs.split(", ")

        moduleType = "broadcaster"        
        name = "broadcaster"

        #print(f"{start} -> {len(start)}")
        if "%" in start or "&" in start: 
            moduleType, name = start[0], start[1:]

        modules[name] = Modul(moduleType, name, outputs)

        #print(f"{start} ({moduleType} {name}): {outputs}")

    # initialize conjunctions
    for modul in modules:
        if modules[modul].type == "&":
            conMemory = {}
            for sender in modules:
                if modules[modul].name in modules[sender].outputs:
                    conMemory[sender] = False
            modules[modul].conMemory = conMemory

    print(len(data))
    print(len(modules))

    modules["button"] = Modul("broadcaster", "button", ["broadcaster"])
   
    pathToRX = []

    for modul in modules:
        print(f"{modul}: {modules[modul]}")
        if "rx" in modules[modul].outputs:
            pathToRX.append(modul)

    print("--------")
    print(pathToRX)

    pathToBefore = []
    for modul in modules:
        if pathToRX[0] in modules[modul].outputs:
            pathToBefore.append((modul, modules[modul].type))

    print("--------")
    print(pathToBefore)
    for (p, _) in pathToBefore:
        ptBefore[p] = None
    print(f"ptBefore: {ptBefore}")
    print(f"TEST {pathToBefore[0] in ptBefore}")

    again = True
    i = 1
    retVal = None

    while True:
    #while again:
        cycle = 1
        if i > 1000 * 20:
            break    
        modules["button"].pressButton() 
        while True:
            #print(f"Cycle {cycle}")
            for modul in modules:
                if modules[modul].processPulse(i) == "rx":
                    retVal = i

            for modul in modules:
                modules[modul].signalReceivedThisCycle = False

            noNext = []
            for modul in modules:
                noNext.append(len(modules[modul].receivedPulses) == 0)
        
            if all(noNext):
                break

            cycle += 1

        hi = 0
        lo = 0

        for modul in modules:
            h, l = modules[modul].getSentSignals()
            hi += h
            lo += l

        hi_all += hi
        lo_all += lo

        allOff = []
        for modul in modules:
            modulType = modules[modul].type
            if modulType == "%":
                allOff.append(modules[modul].flipFlopOn)
                pass
            elif modulType == "&":
                temp = modules[modul]
                allOff.append( all( temp.conMemory[pulse] == Pulse.HIGH for pulse in temp.conMemory))

        #print(f"hi:{hi - hi_before} lo:{lo - lo_before} | {all([val == False for val in allOff])} {i}")
        hi_before = hi
        lo_before = lo

        if all([val == False for val in allOff]):
            again = False
            break

        i += 1


    for p in ptBefore:
        print(f"{p}: {ptBefore[p]}")

    highPulses = 0
    lowPulses = 0

    for modul in modules:
        high, low = modules[modul].getSentSignals()
        highPulses += high
        lowPulses += low
    
    high = (highPulses )
    low = (lowPulses )
    ans = high * low
    
    print(f"low: {low} | high: {high} | {ans} | {retVal}")
    x = 1
    for presses in ptBefore.values():
        x = x * presses // gcd(x, presses)

    ans = x

    return ans    

from time import process_time, sleep
import datetime
from math import gcd 

def main():

    file = open("..\Python\Advent of Code 2023\Day 20\input.txt", 'r')

    data = file.readlines() 
    #data = testData
    #data = testData2

    print(datetime.datetime.now())    

    answer = doIt(data)

    print("-------\n")
    print(int(answer))
    print("\n-------")

    # Part 1
    # 812_046_384 too low
    # 813_307_196 too low
    # 814_934_624 | low: 18361 | high: 44384 | 814934624
    
    # Part 2
    # 1001 too low
    # 228_282_646_835_717
    
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()