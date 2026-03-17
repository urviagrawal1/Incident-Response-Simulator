def handle_action(action, incident, state):
    
    # Monitoring commands
    if action == "check_logs":
        print("\n--- Recent Logs ---")
        for log in incident.logs[-5:]:
            print(log)
        return False

    if action == "check_metrics":
        print("\n--- Metrics ---")
        for k, v in incident.metrics.items():
            print(f"{k}: {v}")
        return False

    # Root cause fix
    if action == incident.root_cause:
        print("✅ Root cause fixed!")
        incident.resolved = True
        return True

    # Symptom fixes
    elif action in incident.valid_actions:
        print("⚠️ Temporary fix applied (symptom fixed, not root cause)")
        state["wrong"] += 1
        return False

    else:
        print("❌ Invalid action")
        state["wrong"] += 1
        return False