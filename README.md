# Unit Converter CLI

This is a command-line interface (CLI) application for converting units of length, weight, temperature, and currency. The application is built using Python and the Typer library.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required dependencies:
   ```
   pip install typer
   ```

## Usage

Run the CLI application using the following command:
```
python cli.py
```

### Commands

#### Convert Length
Convert between different units of length.
```
python cli.py convert-length-cmd <value> <from_unit> <to_unit>
```
Example:
```
python cli.py convert-length-cmd 100 meters kilometers
```

#### Convert Weight
Convert between different units of weight.
```
python cli.py convert-weight-cmd <value> <from_unit> <to_unit>
```
Example:
```
python cli.py convert-weight-cmd 1000 grams kilograms
```

#### Convert Temperature
Convert between different units of temperature.
```
python cli.py convert-temperature-cmd <value> <from_unit> <to_unit>
```
Example:
```
python cli.py convert-temperature-cmd 100 celsius fahrenheit
```

#### Convert Currency
Convert between different currencies.
```
python cli.py convert-currency-cmd <value> <from_currency> <to_currency>
```
Example:
```
python cli.py convert-currency-cmd 100 USD EUR
```

### Supported Units

#### Length
- meters
- kilometers
- centimeters
- millimeters
- miles
- yards
- feet
- inches

#### Weight
- kilograms
- grams
- milligrams
- pounds
- ounces

#### Temperature
- celsius
- fahrenheit
- kelvin

#### Currency
- USD (United States Dollar)
- EUR (Euro)
- GBP (British Pound)
- INR (Indian Rupee)
- AUD (Australian Dollar)
- CAD (Canadian Dollar)
- JPY (Japanese Yen)
- CNY (Chinese Yuan)

## License

This project is licensed under the MIT License.
