from rich.console import Console
from datetime import datetime

console = Console()

def log_event(level, message, incident):
    time = datetime.now().strftime("%H:%M:%S")

    color = {
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red"
    }.get(level, "white")

    formatted = f"[{time}] [{level}] {message}"
    incident.logs.append(formatted)

    console.print(formatted, style=color)