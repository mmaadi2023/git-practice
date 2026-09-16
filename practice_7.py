import sqlite3

conn = sqlite3.connect(":memory:")  # temporary in-memory database
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE listings (
        listing_id INTEGER PRIMARY KEY,
        suburb TEXT,
        price INTEGER
    )
""")

cursor.executemany("INSERT INTO listings (suburb, price) VALUES (?, ?)", [
    ("Richmond", 800000),
    ("Richmond", 820000),
    ("Richmond", 1000000),
    ("Fitzroy", 900000),
    ("Fitzroy", 950000),
])
conn.commit()


cursor.execute("SELECT suburb, price FROM listings")
rows= cursor.fetchall()
print (rows)

def rows-to-dict (rows):

llist = 

for suburb , price in rows:



