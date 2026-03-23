import json
import os

def create_scenario():
    name = input("Scenario name: ")

    stages = []
    print("\nAdd stages (type 'done' to stop):")

    while True:
        delay = input("Delay: ")
        if delay == "done":
            break

        level = input("Level: ")
        msg = input("Message: ")

        stages.append([int(delay), level, msg])

    root_cause = input("\nRoot cause action: ")
    valid_actions = input("Valid actions (comma): ").split(",")

    metrics = {}
    print("\nAdd metrics (key=value, 'done' to stop):")

    while True:
        entry = input("Metric: ")
        if entry == "done":
            break
        k, v = entry.split("=")
        metrics[k.strip()] = v.strip()

    scenario = {
        "name": name,
        "stages": stages,
        "root_cause": root_cause,
        "valid_actions": [a.strip() for a in valid_actions],
        "metrics": metrics
    }

    os.makedirs("scenarios", exist_ok=True)

    path = f"scenarios/{name}.json"
    with open(path, "w") as f:
        json.dump(scenario, f, indent=4)

    print(f"\n✅ Saved at {path}")