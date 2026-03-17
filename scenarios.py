from incident import Incident

def get_scenarios():
    return [
        Incident(
            name="db_failure_chain",
            stages=[
                (1, "INFO", "Connecting to database..."),
                (2, "ERROR", "Database connection failed"),
                (2, "ERROR", "API returning 500"),
                (2, "ERROR", "Frontend failed to load dashboard")
            ],
            root_cause="restart_db",
            valid_actions=["restart_api", "retry"],
            metrics={"cpu": "40%", "db_connections": "0"}
        ),

        Incident(
            name="high_cpu_chain",
            stages=[
                (1, "INFO", "System running normally"),
                (2, "WARNING", "CPU usage 85%"),
                (2, "ERROR", "CPU usage 97%"),
                (2, "ERROR", "Requests timing out")
            ],
            root_cause="scale",
            valid_actions=["restart_service"],
            metrics={"cpu": "97%", "db_connections": "120"}
        ),

        Incident(
            name="network_timeout_chain",
            stages=[
                (1, "INFO", "Calling external API"),
                (2, "WARNING", "Slow response detected"),
                (2, "ERROR", "Timeout error"),
                (2, "ERROR", "Retries exhausted")
            ],
            root_cause="fix_network",
            valid_actions=["retry"],
            metrics={"latency": "3000ms", "packet_loss": "20%"}
        )
    ]