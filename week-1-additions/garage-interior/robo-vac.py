import shutil
import os
import gitit
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
    width = 1
    length = 1
    percentage_battery_remaining = 1000000
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
        print()
        print("PROCEEDING TO VACUUM. PLEASE STAND CLEAR.")
        print()
        print("You stand clear of the little robot and watch it *slowly* move about the garage floor.")
        print("This is clearly going to take a minute, so you run back to your bedroom to take a quick nap.")
        print()
        print("After all, healthy sleep hygiene is terribly important.")
        print("You think you've heard that George Washington was a fan of naps...and you think about that as you doze off...")
        print()
        
        # Sweep the floor...like off the map.
        shutil.rmtree("dirty-garage-floor")

        # Replace with the new workshop space & guidelines documentation
        os.mkdir("workshop")
        gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/garage-interior/workshop/workshop-guidelines.md", "workshop/workshop-guidelines.md")
        
        print("...You spring back awake and run to the garage, eager to see the fruits of your labor.")
        print()
        print("Now that it's clear of junk. The garage feels...bigger. Like, a LOT bigger.")
        print("Like, you could probably fit *entire buildings* in here if you wanted to.")
        print()
        print("You don't have any vehicles to store in here...")
        print("...and admit it, reprogramming that robot vacuum was kinda fun...")
        print("...maybe you'll use this space for your own engineering efforts, like the previous tenant?")
        print()
        print("Speaking of that little vacuum, it whirs to life and chirps out:")
        print("CLEANING COMPLETE. WELCOME BACK TO THE WORKSHOP.")
        print()
        print("The workshop it is, then.")
        

if __name__ == "__main__":
    main()