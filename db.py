import sqlite3

conn = sqlite3.connect("results.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario TEXT,
    time_taken REAL
)
""")

conn.commit()

def save_result(scenario, time_taken):
    cursor.execute(
        "INSERT INTO results (scenario, time_taken) VALUES (?, ?)",
        (scenario, time_taken)
    )
    conn.commit()