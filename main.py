import turtle, random, symbol, user, slotmachine, visuals, time
from definitions import SYMBOLS_REPR, NR_OCURR, GAIN_3X


def main():
    creditsStr = visuals.askInput("How many credits do you want to deposit?\n")
    credits = user.error_credits_check(creditsStr)

    player = user.User(credits)
    my_slotmachine = slotmachine.SlotMachine(SYMBOLS_REPR, NR_OCURR, GAIN_3X)

    while True and not player.stopPlaying():
        keepPlayingStr = visuals.askInput("You have {} credits. Want to stop playing? Press 'y' or 'yes' to stop playing. Otherwise, press any other key.\n".format(player.getCredits()))
        
        if (keepPlayingStr != None and keepPlayingStr.lower() == "y" or keepPlayingStr.lower() == "yes"):
            break
        creditsBet = -1
        visuals.cleanWindow()
        while creditsBet == -1:
            creditsBetStr = visuals.askInput(" > You have {} credits. How many credits do you want to bet on this round?\n".format(player.getCredits()))
            creditsBet = user.error_credits_check(creditsBetStr)
            if not player.canPlay(creditsBet):
                visuals.writeText("You cannot bet more credits that those you have in your possession!\n" +
                    "Tip: steal from one of your fellow betting players, " +
                    "with preference for those who are more rich!\n")
                time.sleep(2)
                visuals.cleanWindow()
                creditsBet = -1
            else:
                my_slotmachine.play(player, creditsBet)
                time.sleep(1)
    visuals.cleanWindow()
    visuals.writeText("See you next time!")
    time.sleep(1)
main()
    

