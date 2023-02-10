import InsectClass as i 


# The main function.
def main():
    insect = i.Insect()


    print('\nThis fly can fly.... (press any button to see)' )
    insect.miles_flown()
    input()

    print(insect.get_length_of_flight(), "mile(s)")
    
            
# Call the main function.
main()
