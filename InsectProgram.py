import InsectClass as i 


# The main function.
def main():

    insect = i.Insect()

    sel = ''
    while sel != 'x':
        print('\nThis fly can fly.... (press any button to see)' )
        insect.miles_flown()
        

        print(insect.get_length_of_flight(), "mile(s)")
        sel = input("Press any button to repeat, or x to exit")

            
# Call the main function.
main()

