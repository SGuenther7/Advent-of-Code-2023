testData = [
    "32T3K 765",
    "KK677 28",
    "QQQJA 483",   
    "KTJJT 220",
    "T55J5 684",
]

"<32T3K,765,1,1>"
"<KTJJT,220,2,2>"
"<KK677,28,2,3>"
"<T55J5,684,3,4>"
"<QQQJA,483,3,5>"

class Hand:
    def __init__(self, cards, bet):
        self.cards = cards
        self.bet = bet
        self.type = -1
        self.rank = -1
    def __repr__(self):
        return (f"<{self.cards},{self.bet},{self.type},{self.rank}>")

    # x == y, 
    def __eq__(self,other):
        return cmp_hand(self, other) == 0
    # x >= y, 
    def __ge__(self,other):
        return cmp_hand(self, other) >= 0
    # x > y, 
    def __gt__(self,other):
        return cmp_hand(self, other) > 0
    # x <= y, 
    def __le__(self,other):
        return cmp_hand(self, other) <= 0
    # x < y, 
    def __lt__(self,other):
        return cmp_hand(self, other) < 0
    # x != y,
    def __ne__(self,other):
        return cmp_hand(self, other) != 0

def cmp_hand(a : Hand, b : Hand):
    ret = 0
    if a.type != b.type : ret = a.type - b.type
    else:
        for i in range(len(a.cards)):
            #print(f"-- {a.cards[i]} {b.cards[i]}")
            if a.cards[i] != b.cards[i]:
                ret = cmp_cards(a.cards[i], b.cards[i])
                #if i == 4:
                #    print(f"{a.cards} {b.cards} {ret}")
                break
                
    #print(f"{a} {b} {ret}")
    
    return ret


def cmp_cards(a : str, b: str):
    val = get_card_val(a) - get_card_val(b)
    return val 

#card_val = "23456789TJQKA"
card_val = "J23456789TQKA"
def get_card_val(card):
    val = card_val.index(card)
    return val

def getType(hand):
    c = {}
    for char in hand:
        val = c.get(char, 0)
        c[char] = val + 1

    highest_type = 0
    l = len(c)
    #print(f"{c} {hand} {l}")
    if l == 1 : 
        #print(f"five of a kind {hand}")
        highest_type = 6
    elif l == 2:
        n = list(c.values())[0]
        #print(f"-- {n}")
        if n == 4 or n == 1: 
            #print(f"fourlets {hand}")
            highest_type = 5
        else: 
            #print(f"full house {hand}")
            highest_type = 4
    elif l == 3:
        d = list(c.values())
        if d[0] == 3 or d[1] == 3 or d[2] == 3: 
            #print(f"triplets {hand}")
            highest_type = 3
        else : 
            #print(f"two pairs {hand}")
            highest_type = 2
    elif l == 4: 
        #print(f"only one {hand}")
        highest_type = 1
        
    num_of_j = c.get("J",0)
    #print(f"{num_of_j} {hand} {highest_type}")
    # print(highest_type)
    if num_of_j > 0:
        # none
        if highest_type == 0:
            highest_type = 1
        # one
        elif highest_type == 1:
            highest_type = 3
        # two
        elif highest_type == 2:
            if num_of_j == 1: highest_type = 4
            elif num_of_j == 2: highest_type = 5
            else: highest_type = -1
        # triple
        elif highest_type == 3:
            highest_type = 5
        # full
        elif highest_type == 4:
            highest_type = 6
        # quad
        elif highest_type == 5:
            highest_type = 6
       # print(f"{hand} {num_of_j}")

    return highest_type

def doIt(data):
    hands = {}
    unique = set()
    for hand in data:
        cards, bet = hand.split(" ")
        h = Hand(cards, int(bet))
        h.type = getType(cards)
        #print(h)
        past = hands.get(h.type, [])
        hands[h.type] = past + [h]
        if len(cards) != 5:
            print(f" - {cards}")
        unique.add(cards)
        
    print("___________")
    for same in hands:
        hands[same].sort()

    last_rank = 1
    for i in range(7): 
        if hands.get(i, False):
            for hand in hands[i]:
                hand.rank = last_rank
                last_rank += 1

    score = 0
    num_score = 0
    sorted_hands = []
    for same in hands:
        for hand in hands[same]:
            score += hand.bet * hand.rank
            num_score += 1
            sorted_hands.append(hand)

    print(f"{len(data)} {num_score} {len(unique)} {len(sorted_hands)}")

    return score

def main():

    file = open("..\Python\Advent of Code 2023\Day 7\Day_7-1_input.txt", 'r')
    data = file.readlines() 
    #data = testData
    #nums = 0
    #print(getType("43334"))
    #print(getType("AAAA7"))
    nums = doIt(data)
    accum = 0

# 252_295_678
    
    print("----")
    print(nums)
    #hand1 = Hand("JKKK2", 1)
    #hand2 = Hand("QQQQ2", 2)
    #print(getType(hand1.cards))
    #print(getType(hand2.cards))
    #print(hand1 < hand2)

    # 250_577_259

if __name__ == "__main__":
    main()