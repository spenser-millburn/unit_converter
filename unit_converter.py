def convert_length(value, from_unit, to_unit):
    length_units = {
        'meters': 1.0,
        'kilometers': 1000.0,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }

    if from_unit not in length_units or to_unit not in length_units:
        raise ValueError("Invalid length unit")

    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'kilograms': 1.0,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }

    if from_unit not in weight_units or to_unit not in weight_units:
        raise ValueError("Invalid weight unit")

    value_in_kilograms = value * weight_units[from_unit]
    return value_in_kilograms / weight_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32

    raise ValueError("Invalid temperature unit")

def convert_currency(value, from_currency, to_currency):
    currency_rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'GBP': 0.75,
        'INR': 74.0,
        'AUD': 1.35,
        'CAD': 1.25,
        'JPY': 110.0,
        'CNY': 6.45
    }

    if from_currency not in currency_rates or to_currency not in currency_rates:
        raise ValueError("Invalid currency")

    value_in_usd = value / currency_rates[from_currency]
    return value_in_usd * currency_rates[to_currency]
