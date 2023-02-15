import random
# dont need to run class definition file but you need to save it, to see changes
# The Coin class simulates a coin that can
# be flipped.


class Coin:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):  # think of self as the instance that you are working with
        self.__sideup = 'Heads'  # attribute initialized to 'Heads' (two underscores makes the attribute private)

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):  # mutator/set method (can change value of attribute)
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
            # separate these two methods because (methods should do one thing at a time)
            # we might want just the value without tossing
            # 6 attributes = 6 set and 6 get methods
    # The get_sideup method returns the value
    # referenced by sideup.

    def get_sideup(self):  # get/accessor method (returns value of attribute)
        return self.__sideup
