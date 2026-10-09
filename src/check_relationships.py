import sqlite3
from pathlib import Path


# ==========================================
# FIND DATABASE
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_FILE = BASE_DIR / "data" / "pharmasense.db"


# ==========================================
# CONNECT
# ==========================================

connection = sqlite3.connect(DATABASE_FILE)

cursor = connection.cursor()


print("\n===================================")
print("PHARMASENSEAI DATA RELATIONSHIPS")
print("===================================")


# ==========================================
# CHECK IMPORTANT TABLES
# ==========================================

tables = [
    "compounds",
    "clinical_trials",
    "trial_sites",
    "lab_results",
    "adverse_events",
    "research_documents"
]


for table in tables:

    print("\n-----------------------------------")
    print("TABLE:", table)
    print("-----------------------------------")

    cursor.execute(f'PRAGMA table_info("{table}")')

    columns = cursor.fetchall()

    for column in columns:
        column_name = column[1]

        # Show columns that look like IDs or relationships
        if (
            "id" in column_name.lower()
            or "compound" in column_name.lower()
            or "trial" in column_name.lower()
        ):
            print("-", column_name)


# ==========================================
# CLOSE
# ==========================================

connection.close()


print("\n===================================")
print("RELATIONSHIP CHECK COMPLETE")
print("===================================")