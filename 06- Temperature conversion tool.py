temperature_c = 25
temperature_f = 77


def celsius_to_fahrenheit(celsius) -> float:
    """Takes a temperature in Celsius and converts it to Fahrenheit."""
    fahrenheit = (celsius * (9 / 5)) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit) -> float:
    """Takes a temperature in Fahrenheit and converts it to Celsius."""
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


def convert_temperature(temperature: float, unit: str) -> float:
    """Takes a temperature value and a unit ('C' for Celsius or 'F' for Fahrenheit)."""
    if unit == "F":
        return fahrenheit_to_celsius(temperature)
    elif unit == "C":
        return celsius_to_fahrenheit(temperature)


converted_f = convert_temperature(temperature_c, "C")
converted_c = convert_temperature(temperature_f, "F")

print(f"{temperature_c}°C is equal to {converted_f}°F")
print(f"{temperature_f}°F is equal to {converted_c}°C")
