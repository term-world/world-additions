def main():
    # Set birth_month equal to your birth month (e.g., Jan = 1, Dec = 12)
    birth_month = input("What month (1-12) were you born? ")

    # Convert birth_month variable into an integer, store the int in the birth_month_number variable
    birth_month_number = int(birth_month)
    
    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    running_number = birth_month_number

    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    running_number = running_number * 3

    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    running_number = running_number + 6

    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    running_number = running_number / 3

    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    first_digit = running_number - birth_month_number

    # TO-DO: DESCRIBE WHAT THE BELOW LINE OF CODE IS DOING
    second_digit = first_digit - 1

    # Display program output to the user
    print()
    print("The first two digits of the door code can be found *within* this program's code...")
    print()

if __name__ == "__main__":
    main()