import sqlite3
from pathlib import Path


# ==========================================
# 1. DATABASE LOCATION
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE = BASE_DIR / "data" / "pharmasense.db"


# ==========================================
# 2. CONNECT TO DATABASE
# ==========================================

connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()


# ==========================================
# 3. ASK USER FOR COMPOUND ID
# ==========================================

print("\n===================================")
print("       PHARMASENSEAI")
print("       COMPOUND SEARCH")
print("===================================")

compound_id = input("\nEnter Compound ID (example: CMP-0001): ").strip()


# ==========================================
# 4. SEARCH COMPOUNDS TABLE
# ==========================================

cursor.execute(
    """
    SELECT *
    FROM compounds
    WHERE compound_id = ?
    """,
    (compound_id,)
)

compound = cursor.fetchone()


# ==========================================
# 5. CHECK RESULT
# ==========================================

if compound is None:

    print("\n❌ Compound not found.")

else:

    print("\n✅ Compound found!")

    print("\n-----------------------------------")
    print("COMPOUND INFORMATION")
    print("-----------------------------------")

    columns = [
        description[0]
        for description in cursor.description
    ]

    for column, value in zip(columns, compound):

        print(f"{column}: {value}")


# ==========================================
# 6. CLOSE DATABASE
# ==========================================

connection.close()


print("\n===================================")
print("SEARCH COMPLETE")
print("===================================")