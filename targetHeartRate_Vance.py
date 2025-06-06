'''
    script: target_heart_rate_Vance.py
    action: a. Calculates target heart rates based off age
            b. Display results
    author: David Vance
    date:   6 June 2025
'''

#global variables
SENTINEL = -99


def input_age():
    '''
    Prompt user for age, then checks for the following conditions:
    - If the age is not an integer, capture the error, print an error
      message and prompt the user for another value
    - If the age is the SENTINEL, print an exit message and exit module
    - If the age does not fall within the expected range of 1 to 110,
      print an error message and prompt the user for another value

    action: Prompt user for age.  Loop while the age is not an integer, is
            not the SENTINEL value, or falls outside of limited values.
            Exit the method when age is an integer and falls within
            allowed range of 1 to 110.
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

            if age == SENTINEL:
                # If age == SENTINEL print message and exit module
                print("\nThank you for using Heart Rate Calculator.\n")
                raise SystemExit

            elif age < 1 or age > 110:
                # Else if age is not in expected range print message and reset input loop
                print("\n*** The age must be between 1 and 110 (or -99 to exit) ***")
                age = ''
    
        except ValueError:
            # Capture error if age is not an integer    
            print("\n*** Your entry must be an integer.  Please try again. ***")
    return age


def determine_target_heart_rates(age):
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
    maximum_target_heart-rate = 220 - age
    low_target_heart_rate = maximum_target_heart_rate * .5     # 50%
    high_target_heart_rate = maximum_target_heart-rate * .85   # 85%

    return low_target_heart_rate, high_target_heart_rate


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

    age = inputAge()
    low_target_heart_rate, high_target_heart_rate = determine_target_heart_rates(age)

    # Display Heart Rate report
    print(f'\nAT AGE {age}')
    print(f'Target heart rate is between {lowTargetHeartRate:.0f} and {highTargetHeartRate:.0f}.')
    print("\nThank you for using Heart Rate Calculator.\n")

    return


if __name__ == '__main__':
    main()
