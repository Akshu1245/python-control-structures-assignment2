# =============================================================================
# Program: Even or Odd Checker
# Description: This program asks the user for an integer and determines
#              whether it is even or odd using an if-else statement.
# Module: Control Structures in Python
# =============================================================================

def main():
    """
    Main function that runs the even/odd checker program.
    """
    
    print("=" * 40)
    print("    EVEN OR ODD CHECKER")
    print("=" * 40)
    
    try:
        # Step 1: Ask the user to enter an integer
        # The input() function always returns a string, so we convert it to int
        user_input = input("\nPlease enter an integer: ")
        number = int(user_input)
        
        # Step 2: Check if the number is even or odd using modulo operator (%)
        # The modulo operator returns the remainder of division
        # If a number divided by 2 has remainder 0, it's even
        # If a number divided by 2 has remainder 1, it's odd
        
        if number % 2 == 0:
            # This block runs if the condition is TRUE (number is even)
            print(f"\n✓ The number {number} is EVEN.")
            print(f"  Explanation: {number} ÷ 2 = {number // 2} with remainder 0")
        else:
            # This block runs if the condition is FALSE (number is odd)
            print(f"\n✓ The number {number} is ODD.")
            print(f"  Explanation: {number} ÷ 2 = {number // 2} with remainder 1")
    
    except ValueError:
        # This block handles the error if user enters something that's not an integer
        # For example: letters, decimals, or special characters
        print("\n✗ Error: Please enter a valid integer (whole number).")
        print("  Examples of valid input: -5, 0, 7, 42")
    
    print("\n" + "=" * 40)
    print("Program finished. Thank you!")
    print("=" * 40)


# This ensures the main() function runs only when this file is executed directly
# and not when it's imported as a module in another file
if __name__ == "__main__":
    main()
