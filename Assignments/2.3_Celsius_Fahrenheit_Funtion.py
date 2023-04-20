#to write the function 
#define the funtion
#call the function

# Define a function to convert Celsius to Fahrenheit
def convertToFahrenheit():

    # Ask the user to input the temperature in Celsius
    print("Enter Temperature in Celsius: ")

    # Read the input from the user and convert it to a float
    celsius = float(input())

    # Calculate the equivalent temperature in Fahrenheit using the formula
    Fahrenheit = (celsius * (9 / 5)) + 32

    # Print the result using string formatting to show both the Celsius and Fahrenheit temperatures
    print(str(celsius) + " degree Celsius is equal to " + str(Fahrenheit) + " degree Fahrenheit.")

# Call the function to convert the temperature
convertToFahrenheit()


