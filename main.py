import click
from simulator import start_simulation

@click.command()
@click.option('--difficulty', default='easy', help='easy / medium / hard')
def run(difficulty):
    start_simulation(difficulty)

if __name__ == "__main__":
    run()