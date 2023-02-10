import InsectClass as i 


# The main function.
def main():

    insect = i.Insect()

    sel = ''
    while sel != 'x':
        print('\nThis insect can fly....')
        insect.miles_flown()
        

        print(insect.get_length_of_flight(), "mile(s)")
        sel = input("Press Enter/Return to repeat, or x to exit")

            
# Call the main function.
main()

