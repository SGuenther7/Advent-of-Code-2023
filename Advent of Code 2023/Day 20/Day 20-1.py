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

    def processPulse(self) -> None:
        #print(f"-- {self.name} {self.receivedPulses}")
        if not self.signalReceivedThisCycle and len(self.receivedPulses) > 0:
            if self.type == "broadcaster":
                self.broadcasterProcess()            
            elif self.type == "%":
                self.flipFlopProcess()
            elif self.type == "&":
                self.conjunctionProcess()
            else:
                print(f"ERROR {self.type}")
            self.receivedPulses.pop(0)
    
    def broadcasterProcess(self):
        self.sendPulses(self.receivedPulses[0])
    
    def flipFlopProcess(self):
        if self.receivedPulses[0] == Pulse.HIGH:
            return
        if self.flipFlopOn:
            p = Pulse.LOW
            self.sendPulses(Pulse.LOW)
            self.flipFlopOn = False
        elif not self.flipFlopOn:
            self.sendPulses(Pulse.HIGH)
            self.flipFlopOn = True
        
    def conjunctionProcess(self):
        #print(self.conMemory.values())
        t = all( self.conMemory[pulse] == Pulse.HIGH for pulse in self.conMemory)
        pulse = Pulse.LOW if t else Pulse.HIGH
        self.sendPulses(pulse)

    def sendPulses(self, pulse):
        for recipient in self.outputs:
            #print(f"{self.name} -{pulse.name}-> {recipient}")
            if recipient in modules:
                modules[recipient].receivePulse(pulse, self.name)

            if pulse == Pulse.HIGH:
                self.sendHigh += 1
            elif pulse == Pulse.LOW:
                self.sendLow += 1
            
    def receivePulse(self, pulse : Pulse, senderName) -> None:
        if self.type == "&":
            self.conMemory[senderName] = pulse
        if len(self.receivedPulses) == 0:
            self.signalReceivedThisCycle = True
        self.receivedPulses.append(pulse)

modules = {}

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
   
    for modul in modules:
        print(f"{modul}: {modules[modul]}")

    again = True
    i = 1
    for _ in range(1_000):
    #while again:
        cycle = 1
        if i > 1000:
            break    
        modules["button"].pressButton() 
        while True:
            #print(f"Cycle {cycle}")
            for modul in modules:
                modules[modul].processPulse()

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

        

        print(f"hi:{hi - hi_before} lo:{lo - lo_before} | {all([val == False for val in allOff])} {i}")
        hi_before = hi
        lo_before = lo


        if all([val == False for val in allOff]):
            again = False
            break
        i += 1

    highPulses = 0
    lowPulses = 0

    for modul in modules:
        high, low = modules[modul].getSentSignals()
        highPulses += high
        lowPulses += low

    pulses = highPulses * lowPulses
    ans = (pulses * 1000 * 1000) / i
    print(f"low: {lowPulses} | high: {highPulses} | {pulses} | {ans}")
    
    high = (highPulses )#* 1000) #/ i
    low = (lowPulses )#* 1000) #/ i
    ans = high * low
    
    print(f"low: {low} | high: {high} | {ans}")
    
    return ans    

from time import process_time, sleep
import datetime

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
    
    t = process_time()
    print(f"elapsed: {(datetime.timedelta( seconds=t ) )}")

if __name__ == "__main__":
    main()