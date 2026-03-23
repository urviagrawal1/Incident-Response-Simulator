import json
import os
from incident import Incident

def get_scenarios():
    return [

        # 1. DB Failure
        Incident(
            name="db_failure_chain",
            stages=[
                (1, "INFO", "Connecting to DB"),
                (2, "ERROR", "DB connection failed"),
                (2, "ERROR", "API returning 500"),
            ],
            root_cause="restart_db",
            valid_actions=["retry", "restart_api"],
            metrics={"cpu": "40%", "db_connections": "0"}
        ),

        # 2. High CPU
        Incident(
            name="high_cpu_chain",
            stages=[
                (1, "INFO", "System normal"),
                (2, "WARNING", "CPU 85%"),
                (2, "ERROR", "CPU 97% - slowdown"),
            ],
            root_cause="scale",
            valid_actions=["restart_service"],
            metrics={"cpu": "97%", "request_rate": "1200rps"}
        ),

        # 3. Memory Leak
        Incident(
            name="memory_leak",
            stages=[
                (1, "INFO", "App running"),
                (2, "WARNING", "Memory usage 85%"),
                (2, "ERROR", "Memory usage 99%"),
            ],
            root_cause="restart_service",
            valid_actions=["scale"],
            metrics={"memory": "99%", "cpu": "60%"}
        ),

        # 4. Network Latency
        Incident(
            name="network_latency",
            stages=[
                (1, "INFO", "Sending request"),
                (2, "WARNING", "Slow response"),
                (2, "ERROR", "Timeout occurred"),
            ],
            root_cause="fix_network",
            valid_actions=["retry"],
            metrics={"latency": "3000ms", "packet_loss": "20%"}
        ),

        # 5. API Crash
        Incident(
            name="api_crash",
            stages=[
                (1, "INFO", "API started"),
                (2, "ERROR", "Unhandled exception"),
                (2, "ERROR", "Service crashed"),
            ],
            root_cause="restart_api",
            valid_actions=["retry"],
            metrics={"error_rate": "90%", "cpu": "30%"}
        ),

        # 6. Cache Failure
        Incident(
            name="cache_failure",
            stages=[
                (1, "INFO", "Fetching from cache"),
                (2, "ERROR", "Cache miss spike"),
                (2, "ERROR", "Increased DB load"),
            ],
            root_cause="restart_cache",
            valid_actions=["retry"],
            metrics={"cache_hit": "10%", "db_connections": "200"}
        ),

        # 7. Disk Full
        Incident(
            name="disk_full",
            stages=[
                (1, "INFO", "Writing logs"),
                (2, "WARNING", "Disk 90%"),
                (2, "ERROR", "Disk full"),
            ],
            root_cause="clear_disk",
            valid_actions=["restart_service"],
            metrics={"disk": "100%"}
        ),

        # 8. Queue Backlog
        Incident(
            name="queue_backlog",
            stages=[
                (1, "INFO", "Queue normal"),
                (2, "WARNING", "Queue delay increasing"),
                (2, "ERROR", "Queue backlog critical"),
            ],
            root_cause="scale_workers",
            valid_actions=["restart_worker"],
            metrics={"queue_size": "10000", "latency": "5000ms"}
        ),

        # 9. DNS Failure
        Incident(
            name="dns_failure",
            stages=[
                (1, "INFO", "Resolving host"),
                (2, "ERROR", "DNS lookup failed"),
            ],
            root_cause="fix_dns",
            valid_actions=["retry"],
            metrics={"dns_latency": "2000ms"}
        ),

        # 10. SSL Issue
        Incident(
            name="ssl_error",
            stages=[
                (1, "INFO", "Connecting HTTPS"),
                (2, "ERROR", "SSL handshake failed"),
            ],
            root_cause="renew_certificate",
            valid_actions=["retry"],
            metrics={"ssl_errors": "100%"}
        ),

        # 11. Thread Explosion
        Incident(
            name="thread_overload",
            stages=[
                (1, "INFO", "Threads normal"),
                (2, "WARNING", "Thread count rising"),
                (2, "ERROR", "Too many threads"),
            ],
            root_cause="fix_threading",
            valid_actions=["restart_service"],
            metrics={"threads": "500"}
        ),

        # 12. Dependency Failure
        Incident(
            name="external_dependency",
            stages=[
                (1, "INFO", "Calling external API"),
                (2, "ERROR", "Dependency unavailable"),
            ],
            root_cause="switch_backup",
            valid_actions=["retry"],
            metrics={"dependency_status": "down"}
        ),

        # 13. Config Error
        Incident(
            name="config_error",
            stages=[
                (1, "INFO", "Loading config"),
                (2, "ERROR", "Invalid config detected"),
            ],
            root_cause="fix_config",
            valid_actions=["restart_service"],
            metrics={"config_errors": "1"}
        ),

        # 14. Auth Failure
        Incident(
            name="auth_failure",
            stages=[
                (1, "INFO", "User login"),
                (2, "ERROR", "Authentication failed"),
            ],
            root_cause="fix_auth",
            valid_actions=["retry"],
            metrics={"login_failures": "95%"}
        ),

        # 15. Rate Limit
        Incident(
            name="rate_limit",
            stages=[
                (1, "INFO", "API usage normal"),
                (2, "ERROR", "Rate limit exceeded"),
            ],
            root_cause="increase_limit",
            valid_actions=["retry"],
            metrics={"requests": "2000/min"}
        ),

        # 16. Service Deadlock
        Incident(
            name="deadlock",
            stages=[
                (1, "INFO", "Processing requests"),
                (2, "ERROR", "Deadlock detected"),
            ],
            root_cause="restart_service",
            valid_actions=["retry"],
            metrics={"cpu": "20%", "latency": "infinite"}
        ),

        # 17. Log Explosion
        Incident(
            name="log_spam",
            stages=[
                (1, "INFO", "Logging normal"),
                (2, "ERROR", "Excessive logging detected"),
            ],
            root_cause="reduce_logging",
            valid_actions=["restart_service"],
            metrics={"log_rate": "10000/s"}
        ),

        # 18. Version Mismatch
        Incident(
            name="version_mismatch",
            stages=[
                (1, "INFO", "Deploying service"),
                (2, "ERROR", "Version incompatibility"),
            ],
            root_cause="rollback",
            valid_actions=["restart_service"],
            metrics={"deploy_errors": "1"}
        ),

        # 19. Load Balancer Issue
        Incident(
            name="lb_failure",
            stages=[
                (1, "INFO", "Routing traffic"),
                (2, "ERROR", "Load balancer failure"),
            ],
            root_cause="restart_lb",
            valid_actions=["retry"],
            metrics={"traffic_drop": "80%"}
        ),

        # 20. Stack Overflow
        Incident(
            name="stack_overflow",
            stages=[
                (2, "WARNING", "Stack is overflowing"),
                (2, "ERROR", "Service crashed"),
            ],
            root_cause="clear_cache",
            valid_actions=["retry", "restart"],
            metrics={"memory": "100%", "cpu": "100%"}
        ),
    ]


def load_custom_scenarios():
    scenarios = []
    folder = "scenarios"

    if not os.path.exists(folder):
        return scenarios

    for file in os.listdir(folder):
        if file.endswith(".json"):
            with open(os.path.join(folder, file)) as f:
                data = json.load(f)
                scenarios.append(
                    Incident(
                        data["name"],
                        data["stages"],
                        data["root_cause"],
                        data["valid_actions"],
                        data.get("metrics", {})
                    )
                )
    return scenarios