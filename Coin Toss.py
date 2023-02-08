# importing name of file (CoinClass.py) [not name of class/dont add .py]
import CoinClass as c


# The main function.
def main():
    # Create an object from the Coin class.
    my_coin = c.Coin()   # this creates an instance called 'my_coin' of the class 'Coin()'
    # his_coin = c.Coin()  # this creates another
    # instance called 'his_coin' of the class 'Coin()'

    # Display the side of the coin that is facing up.
    # calls the get_sideup method
    print('This side is up:', my_coin.get_sideup())
    # notice you do not have to supply the argument/parameter

    # Toss the coin.
    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()

        # Display the side of the coin that is facing up.
        print('This side is up:', my_coin.get_sideup())


# Call the main function.
main()
