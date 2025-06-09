'''
    script determine_target_heart_rate.py
    action: a. Prompt user for age
            b. Validate input for SENTINEL or is not a number
            c. Print lower and upper heart rate numbers
    author: David Vance
    date:   8 June 2025
'''

# Global constants, variables and classes

SENTINEL = 'q'


def calculate_heart_rates(age):
    '''
    Calculate maximum target heart rate from age, then determine the low target heart 
    rate (50%) and the high target heart rate (85%).  

    action: calculate maximum, low target and high target heart rates
    input:  age
    output: none
    return: lower_target_heart_rate, upper_target_heart_rate
    '''

    # Calculate maximum heart rate (220 - age)
    max_heart_rate = 220 - age
    
    # Calculate lower and upper target heart rates (50% to 85% of max)
    lower_target_heart_rate = int(max_heart_rate * 0.50)
    upper_target_heart_rate = int(max_heart_rate * 0.85)
    
    return max_heart_rate, lower_target_heart_rate, upper_target_heart_rate


def is_valid_age(age_string):
    '''
    Input validation to check that the value for age is a number and falls
    between 0 and 120.  If not, return False so the user is prompted to enter
    a value that meets the criteria.

    action: Determine that age is both a number and between 0 and 120.
    input:  age_string
    output: none
    return: True or False
    '''
    # Check if input is a valid integer and in range
    try:
        age = int(age_string)
        # Validate age is within reasonable range (0 to 120)
        return 0 <= age <= 120
    except ValueError:
        return False


# MAIN PROCESSING
# Call to main() function, intitiate processing, print reports, end program

def main():
    '''
    Prompts user for age and compares value entered if value is SENTINEL.
    Passes value entered to validation check.  If check is False it displays
    error message then reprompts user to enter a valid age.  If check is
    True it calculates lower and upper target heart rates and prints 
    report.  It will then loop and prompt user for another age.

    action: Prompt user for age. If value for age == SENTINEL print
            exit message and stop processing, else call function to validate
            age.  If age is not valid, prompt user to enter new value.  If age
            is valid, call function to calculate max, lower and upper heart 
            rates and print results.  Loop while the age is not the SENTINEL
            value.
    input:  age
    output: - Exit message if SENTINEL
            - Error message if age is not number or outside of expected range
            - Max, lower and upper heart rates if age is number and in range
    '''
    
    print("Target Heart Rate Calculator")
    print("Enter your age from 0 to 120 (or 'q' to quit)")
    
    while True:
        age_input = input("Age: ")
        
        # Check for sentinel value to quit by converting input to lower case
        # then compare to SENTINEL value.
        if age_input.lower() == SENTINEL:
            print("Thank you for using Target Heart Rate Calculator.")
            break
            
        # Validate age input
        if not is_valid_age(age_input):
            print("Error: Please enter a valid age (0-120).")
            continue
            
        # Convert valid input to integer
        age = int(age_input)
        
        # Calculate heart rates
        max_heart_rate, lower_target_heart_rate, upper_target_heart_rate = calculate_heart_rates(age)
        
        # Display results
        print(f"\n\033[1mRESULTS FOR AGE {age}:\033[0m")
        print(f"Maximum Heart Rate: {max_heart_rate} beats per minute")
        print(f"Target Heart Rate Range: {lower_target_heart_rate} to {upper_target_heart_rate} beats per minute\n")


if __name__ == "__main__":
    main()