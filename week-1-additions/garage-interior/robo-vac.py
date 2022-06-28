from dotenv import dotenv_values

VARS = dotenv_values('.vac-eq')

def battery_calculator() -> (int, int, float):

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # IMPLEMENT COMPUTATIONS FOR battery_calculator IN SPACE BELOW  #
    
    # TO-DO: ASK USER FOR NECESSARY INPUTS & CONVERT INTO INTEGERS
    # STORE INTEGER INPUTS IN VARIABLES CALLED width AND length


    # TO-DO: COMPUTE THE REMAINING BATTERY PERCENTAGE
    # STORE IT IN A VARIABLE CALLED percentage_battery_remaining
    # HINT: YOU MAY WANT TO CREATE OTHER VARIABLES ALONG THE WAY


    # IMPLEMENT COMPUTATIONS FOR battery_calculator IN SPACE ABOVE  #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    return width, length, percentage_battery_remaining


def main():
    print()
    x, y, b = battery_calculator()
    c = int(VARS["c"])
    d = int(VARS["d"])
    e = int(VARS["e"])
    if b != c - ((((x * y) - c) * d) / e):
        print()
        print("The robot appears to whir to life for a moment, but suddenly a tinny voice shouts:")
        print("CANNOT PROCEED TO VACUUM. DETECTING MALFUNCTIONS IN battery_calculator. PLEASE FIX. PLEASE.")
        print("The robot then immediately shuts down.")
        print()
        print("You must've gotten something wrong with the battery_calculator...better take another look.")
        print()
    else:
        # Will need to program the actual floor-cleaning:
            # Delete the garage-floor folder
            # Replace with the cleaned garage-floor

if __name__ == "__main__":
    main()