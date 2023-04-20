def convert_fahrenheit_to_celsius():
    """
    This function converts a temperature value in Fahrenheit to Celsius.

    It prompts the user to input the temperature in Fahrenheit, reads the input as a float, 
    calculates the equivalent temperature in Celsius using the formula, and prints the result.
    """
    # Prompt the user to enter the temperature in Fahrenheit
    print("Enter temperature in Fahrenheit: ")

    # Read the input as a float
    fahrenheit = float(input())

    # Calculate the equivalent temperature in Celsius using the formula
    celsius = (fahrenheit - 32) * (5 / 9)
    
    # Print the result using string formatting to show both Fahrenheit and Celsius temperatures
    print(f"{fahrenheit} degree Fahrenheit is equal to {celsius} degree Celsius.")

# Call the function to convert the temperature
convert_fahrenheit_to_celsius()