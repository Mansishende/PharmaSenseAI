import pandas as pd
import sqlite3
from pathlib import Path


# ==========================================
# 1. PROJECT PATH
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "synthetic_dataset"

DATABASE_DIR = BASE_DIR / "data"

DATABASE_FILE = DATABASE_DIR / "pharmasense.db"


# ==========================================
# 2. CSV FILES
# ==========================================

files = {
    "compounds": "compounds.csv",
    "clinical_trials": "clinical_trials.csv",
    "trial_sites": "trial_sites.csv",
    "lab_results": "lab_results.csv",
    "adverse_events": "adverse_events.csv",
    "research_documents": "research_documents.csv",
    "agent_interaction_logs": "agent_interaction_logs.csv"
}


# ==========================================
# 3. CREATE DATABASE
# ==========================================

print("\n===================================")
print("PHARMASENSEAI DATABASE CREATION")
print("===================================")

connection = sqlite3.connect(DATABASE_FILE)

print("\nDatabase created at:")
print(DATABASE_FILE)


# ==========================================
# 4. IMPORT CSV FILES
# ==========================================

for table_name, filename in files.items():

    file_path = DATA_DIR / filename

    print("\n-----------------------------------")
    print("Importing:", filename)
    print("-----------------------------------")

    if not file_path.exists():
        print("ERROR: File not found!")
        print(file_path)
        continue

    try:

        df = pd.read_csv(file_path)

        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )

        print("Successfully imported!")
        print("Rows:", len(df))
        print("Columns:", len(df.columns))

    except Exception as e:

        print("ERROR:")
        print(e)


# ==========================================
# 5. CLOSE DATABASE
# ==========================================

connection.close()


print("\n===================================")
print("DATABASE CREATION COMPLETE")
print("===================================")

print("\nDatabase file:")
print(DATABASE_FILE)