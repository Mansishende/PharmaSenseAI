import sqlite3
from pathlib import Path


# ==========================================
# 1. FIND DATABASE
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE = BASE_DIR / "data" / "pharmasense.db"


# ==========================================
# 2. CONNECT TO DATABASE
# ==========================================

connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()


print("\n===================================")
print("PHARMASENSEAI DATABASE TEST")
print("===================================")


# ==========================================
# 3. FIND ALL TABLES
# ==========================================

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name
""")

tables = cursor.fetchall()


print("\nTables found:")
print("-----------------------------------")

for table in tables:
    print("-", table[0])


# ==========================================
# 4. SHOW COLUMNS
# ==========================================

for table in tables:

    table_name = table[0]

    print("\n===================================")
    print("TABLE:", table_name)
    print("===================================")

    cursor.execute(f'PRAGMA table_info("{table_name}")')

    columns = cursor.fetchall()

    print("\nColumns:")

    for column in columns:
        print("-", column[1])


# ==========================================
# 5. CLOSE DATABASE
# ==========================================

connection.close()


print("\n===================================")
print("DATABASE TEST COMPLETE")
print("===================================")