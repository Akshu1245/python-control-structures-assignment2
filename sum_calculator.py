# =============================================================================
# Program: Sum Calculator (1 to 50)
# Description: This program calculates the sum of all numbers from 1 to 50
#              using a for loop.
# Module: Control Structures in Python
# =============================================================================

def main():
    """
    Main function that calculates and displays the sum of numbers from 1 to 50.
    """
    
    print("=" * 50)
    print("    SUM CALCULATOR: Numbers from 1 to 50")
    print("=" * 50)
    
    # Step 1: Initialize a variable to store the running total
    # We start at 0 because we haven't added any numbers yet
    total_sum = 0
    
    # Step 2: Define the range of numbers we want to add
    start_number = 1
    end_number = 50
    
    # Step 3: Use a for loop to iterate through each number
    # range(1, 51) generates numbers: 1, 2, 3, ..., 49, 50
    # Note: range(start, end) goes from 'start' up to but NOT including 'end'
    # So we use 51 to include 50
    
    print("\nCalculating the sum step by step:")
    print("-" * 50)
    
    for current_number in range(start_number, end_number + 1):
        # Add the current number to our running total
        total_sum = total_sum + current_number
        
        # Optional: Show progress every 10 numbers (helps understand the loop)
        if current_number % 10 == 0:
            print(f"  After adding {current_number:2d}: Running total = {total_sum}")
    
    # Step 4: Display the final result
    print("-" * 50)
    print(f"\n✓ RESULT: The sum of numbers from {start_number} to {end_number} is: {total_sum}")
    
    # Bonus: Verify using the mathematical formula
    # Sum = n × (n + 1) / 2, where n is the last number
    formula_result = end_number * (end_number + 1) // 2
    print(f"\n📝 Verification using formula: n×(n+1)/2 = {end_number}×{end_number + 1}/2 = {formula_result}")
    
    if total_sum == formula_result:
        print("   ✓ Both methods give the same answer!")
    
    print("\n" + "=" * 50)
    print("Program finished. Thank you!")
    print("=" * 50)


# This ensures the main() function runs only when this file is executed directly
if __name__ == "__main__":
    main()
