def FahrenheitToCelsius(temp):
    if isinstance(temp, (int, float)):
        return (temp - 32.0) * (5.0 / 9.0)

def CelsiusToFahrenheit(temp):
    if isinstance(temp, (int, float)):
        return temp / (5.0 / 9.0) + 32.0
