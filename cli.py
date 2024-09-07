import typer
from unit_converter import convert_length, convert_weight, convert_temperature

app = typer.Typer()

@app.command()
def convert_length_cmd(value: float, from_unit: str, to_unit: str):
    result = convert_length(value, from_unit, to_unit)
    typer.echo(f"{value} {from_unit} is {result} {to_unit}")

@app.command()
def convert_weight_cmd(value: float, from_unit: str, to_unit: str):
    result = convert_weight(value, from_unit, to_unit)
    typer.echo(f"{value} {from_unit} is {result} {to_unit}")

@app.command()
def convert_temperature_cmd(value: float, from_unit: str, to_unit: str):
    result = convert_temperature(value, from_unit, to_unit)
    typer.echo(f"{value} {from_unit} is {result} {to_unit}")

if __name__ == "__main__":
    app()


