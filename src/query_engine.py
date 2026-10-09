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

print()
print("==========================================")
print("           PHARMASENSEAI")
print("             QUERY ENGINE")
print("==========================================")

compound_id = input(
    "\nEnter Compound ID (example: CMP-0001): "
).strip()


# ==========================================
# 4. GET ALL DATABASE TABLES
# ==========================================

cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    AND name NOT LIKE 'sqlite_%'
""")

tables = cursor.fetchall()


print()
print("==========================================")
print("SEARCHING DATABASE")
print("==========================================")


found_something = False


# ==========================================
# 5. SEARCH EVERY TABLE
# ==========================================

for table_row in tables:

    table_name = table_row["name"]

    # Get columns
    cursor.execute(
        f'PRAGMA table_info("{table_name}")'
    )

    columns = cursor.fetchall()

    column_names = [
        column["name"]
        for column in columns
    ]

    # --------------------------------------
    # Search if compound_id exists
    # --------------------------------------

    if "compound_id" in column_names:

        cursor.execute(
            f'''
            SELECT *
            FROM "{table_name}"
            WHERE compound_id = ?
            ''',
            (compound_id,)
        )

        rows = cursor.fetchall()

        if rows:

            found_something = True

            print()
            print("------------------------------------------")
            print("TABLE:", table_name)
            print("RECORDS FOUND:", len(rows))
            print("------------------------------------------")

            for row in rows[:5]:

                print()

                for column in row.keys():

                    print(
                        f"{column}: {row[column]}"
                    )

            if len(rows) > 5:

                print()
                print(
                    f"... and {len(rows) - 5} more records"
                )


# ==========================================
# 6. RESULT
# ==========================================

print()
print("==========================================")

if found_something:

    print("SEARCH SUCCESSFUL")
    print("Compound information was found.")

else:

    print("NO INFORMATION FOUND")
    print(
        f"No database records found for {compound_id}."
    )

print("==========================================")


# ==========================================
# 7. CLOSE DATABASE
# ==========================================

connection.close()