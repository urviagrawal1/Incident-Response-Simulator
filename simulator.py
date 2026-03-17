import threading
import time
import random
from scenarios import get_scenarios
from logger import log_event
from actions import handle_action


def run_incident(incident):
    for delay, level, message in incident.stages:
        if incident.resolved:
            break
        time.sleep(delay)
        log_event(level, message, incident)


def start_simulation(difficulty):
    scenarios = get_scenarios()

    # Difficulty scaling
    if difficulty == "easy":
        incident = random.choice(scenarios[:1])
    elif difficulty == "medium":
        incident = random.choice(scenarios[:2])
    else:
        incident = random.choice(scenarios)

    print(f"\n🚀 Scenario: {incident.name} ({difficulty})\n")

    # Start background thread
    thread = threading.Thread(target=run_incident, args=(incident,))
    thread.start()

    start_time = time.time()
    state = {"wrong": 0}

    # User loop
    while not incident.resolved:
        action = input("\nAction (check_logs / check_metrics / restart_db / restart_api / retry / scale / fix_network / exit): ").strip()

        if action == "exit":
            print("❌ Exiting simulation")
            return

        resolved = handle_action(action, incident, state)

        if resolved:
            break

    end_time = time.time()
    time_taken = round(end_time - start_time, 2)

    # Scoring
    score = max(0, 100 - (time_taken * 2) - (state["wrong"] * 5))

    print("\n🏁 INCIDENT RESOLVED")
    print(f"⏱️ Time: {time_taken}s")
    print(f"❌ Mistakes: {state['wrong']}")
    print(f"⭐ Score: {score}")

    # Feedback
    if state["wrong"] == 0:
        print("🔥 Perfect debugging!")
    elif state["wrong"] < 3:
        print("👍 Good job, but can improve")
    else:
        print("⚠️ Too many incorrect attempts")