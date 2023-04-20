#convertToCelsius()

# Define a function to convert Fahrenheit to Celsius
def convertToCelsius():

    # Ask the user to input the temperature in Fahrenheit
    print("Enter Temperature in Fahrenheit: ")

    # Read the input from the user and convert it to a float
    Fahrenheit = float(input())

    # Calculate the equivalent temperature in Celsius using the formula
    Celsius = (Fahrenheit - 32) * (5 / 9)
    
    # Print the result using string formatting to show both the Fahrenheit and Celsius temperatures
    print(str(Fahrenheit) + " degree Fahrenheit is equal to " + str(Celsius) + " degree Celsius.")

# Call the function to convert the temperature
convertToCelsius()