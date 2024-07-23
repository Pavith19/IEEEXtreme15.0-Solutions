

games = int(input())
for game in range(games):
    rounds = int(input())
    # list of tuples 
    # value that Alice rolled, and the value that Bob rolled in one round.
    sixesbyD1 = 0
    sixesbyD2 = 0
    alice = 0
    bob = 0
    swapped = False
    for round in range(rounds):
        in1, in2 = [int(x) for x in input().split()]
        alice += in1
        bob += in2
        if (in1==6 and not swapped) or (in2==6 and swapped):
            sixesbyD1 +=1
        if (in1==6 and swapped) or (in2==6 and not swapped):
            sixesbyD2 +=1
        if alice != bob:
            swapped = not swapped
    if sixesbyD1 > sixesbyD2:
        print("1")
    else:
        print("2")



    # claculate number of sixes given by each dice
