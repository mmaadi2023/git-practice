import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE agents (
        agent_id INTEGER PRIMARY KEY,
        agent_name TEXT,
        region TEXT
    )
""")

cursor.execute("""
    CREATE TABLE listings (
        listing_id INTEGER PRIMARY KEY,
        suburb TEXT,
        price INTEGER,
        agent_id INTEGER,
        listed_date TEXT
    )
""")

cursor.executemany("INSERT INTO agents (agent_name, region) VALUES (?, ?)", [
    ("Alice", "North"),
    ("Bob", "South"),
    ("Carol", "North"),
])

cursor.executemany("INSERT INTO listings (suburb, price, agent_id, listed_date) VALUES (?, ?, ?, ?)", [
    ("Richmond", 800000, 1, "2026-01-10"),
    ("Richmond", 820000, 1, "2026-02-15"),
    ("Fitzroy", 1000000, 2, "2026-01-20"),
    ("Fitzroy", 950000, 2, "2026-03-01"),
    ("Carlton", 700000, 3, "2026-02-05"),
    ("Carlton", None, 3, "2026-02-10"),  # missing price, for later NULL exercise
])
conn.commit()

# --- write your SQL below ---
cursor.execute(" SELECT listings.suburb, listings.price, listings.listed_date, agents.agent_name FROM listings join agents on listings.agent_id = agents.agent_id ")
rows = cursor.fetchall()
for row in rows:
    print(row)