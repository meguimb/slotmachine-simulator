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
    while True and credits != -1:
        keepPlayingStr = input(" > You have {} credits. Want to stop playing? Press 'y' or 'yes' to stop playing. Otherwise, press any other key.\n".format(credits))
        if (keepPlayingStr.lower() == "y" or keepPlayingStr.lower() == "yes"):
            break
        creditsBet = -1
        while creditsBet == -1:
            creditsBetStr = input(" > How many credits do you want to bet on this round?\n")
            creditsBet = error_credits_check(creditsBetStr)
            if creditsBet > credits:
                print(" > You cannot bet more credits that those you have in your possession!")
                print("Tip: steal from one of your fellow betting players, with preference for those who are more rich!\n")
            creditsBet = -1

main()

class User:
    def __init__(credits):
        self.credits = credits

    def depositCredits(credits):
        return 0
    
    def withdraw(credits):
        return 0

class SlotMachine:
    symbols = [i for i in range(7)]
    symbolsRepr = ['0', "?", "X", "@", "$", "£", "€"]
    nrOcurr = [50, 40, 30, 20, 10, 5, 1]
    sgain3x = [5, 10, 20, 70, 200, 1000, 100000]
    slots = [-1 for i in range(3)]
    def __init__():
        return 0
    
    def spin():
        self.slots = list(random.choices(self.symbols, weights=self.nrOcurr, k=3))

    def getPayout(creditsBetted):
        if self.slots.count(self.slots[0]) == 3:
            return creditsBetted * self.gain3x[self.slots[0]]
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

# random.choices(symbols, weights=nrOcurr, k=3)
    

