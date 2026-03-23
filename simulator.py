import threading
import time
import random
from scenarios import get_scenarios, load_custom_scenarios
from logger import log_event
from actions import handle_action

def run_incident(incident):
    for delay, level, msg in incident.stages:
        if incident.resolved:
            break
        time.sleep(delay)
        log_event(level, msg, incident)

def start_simulation(difficulty):
    scenarios = get_scenarios() + load_custom_scenarios()

    if not scenarios:
        print("No scenarios available")
        return

    incident = random.choice(scenarios)

    print(f"\n🚀 Scenario: {incident.name}\n")

    thread = threading.Thread(target=run_incident, args=(incident,))
    thread.start()

    start_time = time.time()
    state = {"wrong": 0}

    while not incident.resolved:
        available_actions = (
            ["check_logs", "check_metrics"]
            + incident.valid_actions
            + [incident.root_cause]
            + ["exit"]
        )

        action = input(f"\nAction ({'/'.join(available_actions)}): ").strip()

        if action == "exit":
            return

        resolved = handle_action(action, incident, state)

        if resolved:
            break

    time_taken = round(time.time() - start_time, 2)
    score = max(0, 100 - (time_taken * 2) - (state["wrong"] * 5))

    print("\n🏁 RESOLVED")
    print(f"⏱ Time: {time_taken}s")
    print(f"❌ Mistakes: {state['wrong']}")
    print(f"⭐ Score: {score}")