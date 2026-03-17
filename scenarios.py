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
        ),

        Incident(
            name="memory_leak_chain",
            stages=[
                (1, "INFO", "Service started"),
                (2, "WARNING", "Memory usage increasing"),
                (2, "ERROR", "Memory usage at 95%"),
                (2, "ERROR", "Service crashed due to OOM")
            ],
            root_cause="restart_service",
            valid_actions=["scale"],
            metrics={"memory": "95%", "cpu": "40%"}
        ),

        Incident(
            name="disk_full_chain",
            stages=[
                (1, "INFO", "Writing logs"),
                (2, "WARNING", "Disk usage at 85%"),
                (2, "ERROR", "Disk full"),
                (2, "ERROR", "Cannot write logs / service failing")
            ],
            root_cause="clear_disk",
            valid_actions=["restart_service"],
            metrics={"disk": "100%", "cpu": "30%"}
        ),

        Incident(
            name="auth_failure_chain",
            stages=[
                (1, "INFO", "User login attempt"),
                (2, "WARNING", "Token validation failed"),
                (2, "ERROR", "Unauthorized access (401)"),
                (2, "ERROR", "Multiple auth failures detected")
            ],
            root_cause="refresh_token",
            valid_actions=["retry"],
            metrics={"auth_errors": "high", "requests": "normal"}
        )
    ]