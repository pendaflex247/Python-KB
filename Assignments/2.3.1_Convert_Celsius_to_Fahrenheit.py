def convert_celsius_to_fahrenheit():
    """
    This function converts a temperature value in Celsius to Fahrenheit.

    It prompts the user to input the temperature in Celsius, reads the input as a float, 
    calculates the equivalent temperature in Fahrenheit using the formula, and prints the result.
    """
    # Prompt the user to enter the temperature in Celsius
    print("Enter temperature in Celsius: ")

    # Read the input as a float
    celsius = float(input())

    # Calculate the equivalent temperature in Fahrenheit using the formula
    fahrenheit = (celsius * (9 / 5)) + 32
    
    # Print the result using string formatting to show both Celsius and Fahrenheit temperatures
    print(f"{celsius} degree Celsius is equal to {fahrenheit} degree Fahrenheit.")

# Call the function to convert the temperature
convert_celsius_to_fahrenheit()
