from definitions import SYMBOLS_REPR, NR_OCURR, GAIN_3X
# 1 classe - uma slot machine ou as 3 slot machines numa classe
# 1 classe - 

def error_credits_check(credits_str):
    if credits_str.isnumeric() is False:
        print("ERROR: The number of credits you wrote is invalid. Try Again!")
        return -1
    return int(credits_str)


def main():
    creditsStr = input(" > How many credits do you want to deposit?\n")
    credits = error_credits_check(creditsStr)

    player = User(credits)
    my_slotmachine = SlotMachine(SYMBOLS_REPR, NR_OCURR, GAIN_3X)

    while True and player.getCredits() != -1:
        keepPlayingStr = input(" > You have {} credits. Want to stop playing? Press 'y' or 'yes' to stop playing. Otherwise, press any other key.\n".format(credits))
        if (keepPlayingStr.lower() == "y" or keepPlayingStr.lower() == "yes"):
            break
        creditsBet = -1
        while creditsBet == -1:
            creditsBetStr = input(" > How many credits do you want to bet on this round?\n")
            creditsBet = error_credits_check(creditsBetStr)
            if player.canPlay(creditsBet):
                print(" > You cannot bet more credits that those you have in your possession!")
                print("Tip: steal from one of your fellow betting players, with preference for those who are more rich!\n")
                creditsBet = -1
            else:
                # make a round


main()

class User:
    def __init__(credits):
        self.credits = credits
    
    def getCredits(self):
        return self.credits

    def depositCredits(self, credits):
        return 0
    
    def withdraw(self, credits):
        return 0
    
    def canPlay(self, creditsBet):
        return creditsBet < self.credits
    # keep track of wins, loses, amount betted, amount won/lost

class SlotMachine:
    slots = [-1 for i in range(3)]
    def __init__(self, symbols_repr, nr_ocurr, gain_3x):
        self.symbols = createSlotSymbols(symbols_repr, nr_ocurr, gain_3x)
        return 0
    
    def spin():
        self.slots = list(random.choices(self.symbols, weights=NR_OCURR, k=3))

    def getPayout(creditsBetted):
        if self.slots.count(self.slots[0]) == 3:
            return creditsBetted * self.slots[0].getGain()
        return 0

class Symbol:
    def __init__(self, symbolRepr, nOcurr, gain3x):
        self.repr = symbolRepr
        self.nOcurr = nOcurr
        self.gain3x = gain3x
    def __repr__(self):
        return self.repr

    def getWeight(self):
        return self.nOcurr

    def getGain(self):
        return self.gain3x

"""
createSlotSymbols creates the list of symbols (of type Symbol) to be used in the slot machine
"""
def createSlotSymbols(symbols_repr, nr_ocurr, gain_3x):
    symbolsList = []
    for i in range(7):
        symbolsList[i] = Symbol(symbols_repr[i], nr_ocurr[i], gain_3x[i])
    return symbolsList

# random.choices(symbols, weights=nrOcurr, k=3)
    

