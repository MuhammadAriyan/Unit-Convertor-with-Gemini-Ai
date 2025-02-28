
class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            'meters_to_feet': 3.28084,
            'feet_to_meters': 0.3048,
            'kilograms_to_pounds': 2.20462,
            'pounds_to_kilograms': 0.453592,
            # Add more conversion factors as needed
        }

    def convert(self, value, from_unit, to_unit):
        key = f'{from_unit}_to_{to_unit}'
        if key in self.conversion_factors:
            return value * self.conversion_factors[key]
        else:
            raise ValueError(f'Conversion from {from_unit} to {to_unit} not supported.')

# Example usage:
if __name__ == "__main__":
    converter = UnitConverter()
    print(converter.convert(10, 'meters', 'feet'))  # Output: 32.8084
    print(converter.convert(5, 'kilograms', 'pounds'))  # Output: 11.0231
