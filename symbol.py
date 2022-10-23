class Symbol:
    def __init__(self, symbolRepr, nOcurr, gain3x):
        self.repr = symbolRepr
        self.nOcurr = nOcurr
        self.gain3x = gain3x

    def __str__(self):
        return " " + self.repr + " "

    def __repr__(self):
        return " " + str(self) + " "

    def getWeight(self):
        return self.nOcurr

    def getGain(self):
        return self.gain3x
    
    def getVisualRepr(self):
        return self.repr

"""
createSlotSymbols creates the list of symbols (of type Symbol) to be used in the slot machine
"""
def createSlotSymbols(symbols_repr, nr_ocurr, gain_3x):
    symbolsList = [0 for i in range(7)]
    for i in range(7):
        symbolsList[i] = Symbol(symbols_repr[i], nr_ocurr[i], gain_3x[i])
    return symbolsList