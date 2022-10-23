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
    self.symbols = ['0', "?", "X", "@", "$", "£", "€"]
    self.nrOcurr = [50, 40, 30, 20, 10, 5, 1]
    self.gain3x = [5, 10, 20, 70, 200, 1000, 100000]
    self.slots = []
    def __init__():
        return 0
