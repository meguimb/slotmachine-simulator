class User:
    history = []
    def __init__(self, credits):
        self.credits = credits
    
    def getCredits(self):
        return self.credits

    def deposit(self, credits):
        self.history.append(['+', credits])
        self.credits = self.credits + credits
    
    def withdraw(self, credits):
        self.history.append(['-', credits])
        self.credits = self.credits - credits
    
    def canPlay(self, creditsBet):
        return creditsBet <= self.credits
    
    def stopPlaying(self):
        return self.credits <= 0

    def printHistory(self):
        print(*self.history, sep=", ")
        return 0

def error_credits_check(credits_str):
    if credits_str.isnumeric() is False:
        print("ERROR: The number of credits you wrote is invalid. Try Again!")
        return -1
    elif int(credits_str) <= 0:
        print("ERROR: You have to bet a positive amount of credits!")
        return -1

    return int(credits_str)