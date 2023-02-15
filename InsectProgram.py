import InsectClass as i 


# The main function.
def main():

    mosquito = i.Insect('mosquito',2,4)
    houseFly = i.Insect('houseFly',2,4)



    sel = ''
    while sel != 'x':
        print('\nThe', mosquito.get_name(), 'can fly....')
        mosquito.flight_length()
        print(mosquito.get_length_of_flight(), "mile(s)")

        print('\nThe', houseFly.get_name(), 'house fly can fly....')
        houseFly.flight_length()
        print(houseFly.get_length_of_flight(), "mile(s)")
        
        sel = input("Press Enter/Return to repeat, or x to exit")

            
# Call the main function.
main()

