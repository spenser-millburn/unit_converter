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

