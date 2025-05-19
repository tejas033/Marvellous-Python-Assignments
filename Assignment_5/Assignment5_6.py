# Assignment5_6.py

# Celsius to Fahrenheit converter

def CelsiusToFahrenheit(intCelsius):
    return ((intCelsius * 9/5) + 32)

def main():
    tempInCel = int(input("Enter temperature in Celsius: "))
    print(f"Temperature in Fahrenheit: {CelsiusToFahrenheit(tempInCel)}\u00B0F")

if __name__ == "__main__":
    main()