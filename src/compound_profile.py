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
connection.row_factory = sqlite3.Row

cursor = connection.cursor()


# ==========================================
# 3. GET COMPOUND ID
# ==========================================

print("\n===================================")
print("       PHARMASENSEAI")
print("       COMPOUND PROFILE")
print("===================================")

compound_id = input(
    "\nEnter Compound ID (example: CMP-0001): "
).strip()


# ==========================================
# 4. FIND COMPOUND
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


if compound is None:

    print("\n❌ Compound not found.")

    connection.close()

    exit()


# ==========================================
# 5. SHOW COMPOUND INFORMATION
# ==========================================

print("\n===================================")
print("COMPOUND INFORMATION")
print("===================================")

for key in compound.keys():

    print(f"{key}: {compound[key]}")


# ==========================================
# 6. CHECK OTHER TABLES
# ==========================================

tables = [
    "clinical_trials",
    "lab_results",
    "adverse_events"
]


for table in tables:

    print("\n===================================")
    print(table.upper())
    print("===================================")

    # Get table columns
    cursor.execute(
        f'PRAGMA table_info("{table}")'
    )

    columns = cursor.fetchall()

    column_names = [
        column["name"]
        for column in columns
    ]

    # Only search if the table contains compound_id
    if "compound_id" in column_names:

        cursor.execute(
            f"""
            SELECT *
            FROM "{table}"
            WHERE compound_id = ?
            """,
            (compound_id,)
        )

        rows = cursor.fetchall()

        if len(rows) == 0:

            print("No records found.")

        else:

            print("Records found:", len(rows))

            for row in rows[:10]:

                print("\n-----------------------------")

                for key in row.keys():

                    print(f"{key}: {row[key]}")

            if len(rows) > 10:

                print(
                    f"\nShowing first 10 of {len(rows)} records."
                )

    else:

        print(
            "This table does not have a compound_id column."
        )


# ==========================================
# 7. CLOSE DATABASE
# ==========================================

connection.close()


print("\n===================================")
print("COMPOUND PROFILE COMPLETE")
print("===================================")