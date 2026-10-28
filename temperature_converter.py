tempcel = float(input("What's the temperature in Celsius? "))
def celsius_to_fahrenheit(tempcel) :
    return tempcel * 9/5 + 32
tempfar = celsius_to_fahrenheit(tempcel)
print(f"Temperature in Fahrenheit: {tempfar:.1f}")