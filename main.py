import turtle, random, symbol, user, slotmachine, visuals
from definitions import SYMBOLS_REPR, NR_OCURR, GAIN_3X


def main():
    creditsStr = visuals.askInput("How many credits do you want to deposit?\n")
    credits = user.error_credits_check(creditsStr)

    player = user.User(credits)
    my_slotmachine = slotmachine.SlotMachine(SYMBOLS_REPR, NR_OCURR, GAIN_3X)

    while True and not player.stopPlaying():
        keepPlayingStr = visuals.askInput("You have {} credits. Want to stop playing? Press 'y' or 'yes' to stop playing. Otherwise, press any other key.\n".format(player.getCredits()))
        # keepPlayingStr = input(" > You have {} credits. Want to stop playing? Press 'y' or 'yes' to stop playing. Otherwise, press any other key.\n".format(player.getCredits()))
        if (keepPlayingStr.lower() == "y" or keepPlayingStr.lower() == "yes"):
            break
        creditsBet = -1
        while creditsBet == -1:
            creditsBetStr = visuals.askInput(" > You have {} credits. How many credits do you want to bet on this round?\n".format(player.getCredits()))
            creditsBet = user.error_credits_check(creditsBetStr)
            if not player.canPlay(creditsBet):
                visuals.writeText("You cannot bet more credits that those you have in your possession!")
                visuals.writeText("Tip: steal from one of your fellow betting players, with preference for those who are more rich!\n")
                creditsBet = -1
            else:
                my_slotmachine.play(player, creditsBet)
    if (my_slotmachine.getNumberOfRounds() != 0):
        if (player.getCredits() == 0):
            visuals.writeText("You are not allowed in this casino no longer.", end="") 
        visuals.writeText("Here's your betting history: ")
        player.printHistory()
        visuals.writeText("And here's the track of symbols in the slot machine while you played with us: ")
        my_slotmachine.printHistory()
    else:
        visuals.writeText("It's a shame you didn't play any round! Come back soon!")

main()
# visuals.drawSlots(["$", "@", "?"])
# visuals.writeText("You are not allowed in this casino no longer.")
    

