import click
from simulator import start_simulation
from builder import create_scenario
from scenarios import get_scenarios

@click.group()
def cli():
    pass

@cli.command()
@click.option('--difficulty', default='easy')
def run(difficulty):
    start_simulation(difficulty)

@cli.command()
def build():
    create_scenario()

if __name__ == "__main__":
    cli()