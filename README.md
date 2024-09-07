# CLI Unit Converter

This is a command-line interface (CLI) application for converting units of length, weight, and temperature using the `typer` library.

## Installation

1. Clone the repository:
   ```
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```
   cd <project_directory>
   ```
3. Install the required dependencies:
   ```
   pip install typer unit_converter
   ```

## Usage

Run the CLI application using the following command:
```
python cli.py
```

### Commands

- Convert Length:
  ```
  python cli.py convert-length <value> <from_unit> <to_unit>
  ```
  Example:
  ```
  python cli.py convert-length 100 meters feet
  ```

- Convert Weight:
  ```
  python cli.py convert-weight <value> <from_unit> <to_unit>
  ```
  Example:
  ```
  python cli.py convert-weight 70 kilograms pounds
  ```

- Convert Temperature:
  ```
  python cli.py convert-temperature <value> <from_unit> <to_unit>
  ```
  Example:
  ```
  python cli.py convert-temperature 100 celsius fahrenheit
  ```
