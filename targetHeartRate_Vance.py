'''
    script: targetHeartRate_Vance.py
    action: a. Calculates target heart rates based off age
            b. Display results
    author: David Vance
    date: 22 January 2025
'''

#global variables
SENTINEL = -99


def inputAge():
    '''
    Prompt user for age, confirm it is an integer value, and confirm it 
    falls within expected range of 1 to 110.

    action: Prompt user for age, confirm input is an integer and falls
            within expected range.
    input:  age
    output: entry prompt, error message (if needed)
    return: age
    '''
    # local variables
    age = ''

    # Loop while age has a null value
    while not age:
        try: 
            # Prompt user for age as an integer
            age = int(input("Enter an age between 1 and 110 (or -99 to exit): "))
            if age < 1 or age > 110:
                print("\n*** The age must be between 1 and 110 (or -99 to exit) ***")
                age = ''  # If age out of range loop again
        except ValueError:
            # Capture error if age is not an integer, set age to null value
            print("\n*** Your entry must be an integer.  Please try again. ***")
    return age


def determineAge():
    '''
    Call inputAge to get an age value, then determine if it is:
    - The SENTINEL value (if so, print exit message and quit)
    - If it is within expected age, return the age value

    action: call inputAge to get age, validate age for SENTINEL or in range
    input:  age from inputAge function
    output: exit message
    return: age
    '''
    # call inputAge
    age = inputAge()

    # If age is not within expected value either exit or reenter age
    # while age < 1 or age > 110:
    if age == SENTINEL:
        print("\nThank you for using Heart Rate Calculator.\n")
        raise SystemExit

    # Age is within expected value return age to main()
    return age


def determineTargetHeartRates(age):
    '''
    Calculate maximum target heart rate from age, then determine the low target heart 
    rate (50%) and the high target heart rate (85%).  

    action: calculate maximum, low target and high target heart rates
    input:  age
    output: none
    return: lowTargetHeartRate, highTargetHeartRate
    '''
    # Calculate the maximum heart rate first (220 - age), then calculate the 
    # low target heart rate (50%) and high target heart rate (85%) from the
    # maximum heart rate.
    maximumTargetHeartRate = 220 - age
    lowTargetHeartRate = maximumTargetHeartRate * .5     # 50%
    highTargetHeartRate = maximumTargetHeartRate * .85   # 85%

    return lowTargetHeartRate, highTargetHeartRate


# MAIN PROCESSING
# Call to main() function, intitiate processing, print reports, end program

def main():
    '''
    Inputs the age from the user, conducts input validation, calculates the
    target heart rate values, and then prints a report.  All of this is done
    through function calls; no calculations are done in the main function.

    action: Calculate target heart rate
    input:  None
    output: Display Heart Rate report
    return: None
    '''

    age = determineAge()
    lowTargetHeartRate, highTargetHeartRate = determineTargetHeartRates(age)

    # Display Heart Rate report
    print(f'\nAT AGE {age}')
    print(f'Target heart rate is between {lowTargetHeartRate:.0f} and {highTargetHeartRate:.0f}.')
    print("\nThank you for using Heart Rate Calculator.\n")

    return


if __name__ == '__main__':
    main()
