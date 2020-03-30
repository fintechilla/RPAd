from lackey import *

def main(n):

    wait(3)
    wait("ErrorLoadingException136.png", 10)
    wait(1)

    if exists("ErrorLoadingException136.png"):

        click("OK135.png")
        wait(1)

    else:
        print("{} No ErrorLoadingException".format(n))

# main()