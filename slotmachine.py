import random, symbol, visuals

class SlotMachine:
    history = []
    slots = [-1 for i in range(3)]
    def __init__(self, symbols_repr, nr_ocurr, gain_3x):
        self.symbols = symbol.createSlotSymbols(symbols_repr, nr_ocurr, gain_3x)
        self.nr_ocurr = nr_ocurr

    def getPayout(self, creditsBetted):
        payout = 0
        if self.slots.count(self.slots[0]) == 3:
            payout = creditsBetted * self.slots[0].getGain()
            visuals.writeText(":) You won {} credits. Right on!".format(payout))
        else:
            visuals.writeText(":( Sorry! It seems like you've lost your initial bet!")
        return payout
    
    def spin_result_repr(self):
        slots_symbols = [s.getVisualRepr() for s in self.slots]
        return [s for s in slots_symbols]
    
    def spin(self):
        self.slots = list(random.choices(self.symbols, weights=self.nr_ocurr, k=3))
        visuals.drawSlots(self.spin_result_repr())
        self.history.append([self.slots])

    def play(self, player, current_bet):
        player.withdraw(current_bet)
        self.spin()

        gains = self.getPayout(current_bet)
        player.deposit(gains)
    
    def printHistory(self):
        print(*self.history, sep=", ")
        return 0
    
    def getNumberOfRounds(self):
        return len(self.history)