import pandas as pd
from pathlib import Path


# ==========================================
# 1. FIND PROJECT FOLDER
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

# Your CSV files are inside:
# data/synthetic_dataset
DATA_DIR = BASE_DIR / "data" / "synthetic_dataset"


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
# 3. LOAD THE DATA
# ==========================================

datasets = {}

for name, filename in files.items():

    file_path = DATA_DIR / filename

    print("\n-----------------------------------")
    print("Loading:", filename)
    print("-----------------------------------")

    if not file_path.exists():
        print("ERROR: File not found!")
        print("Expected location:", file_path)
        continue

    try:
        df = pd.read_csv(file_path)

        datasets[name] = df

        print("Successfully loaded!")
        print("Rows:", len(df))
        print("Columns:", len(df.columns))

    except Exception as e:
        print("ERROR while reading file:")
        print(e)


# ==========================================
# 4. SHOW SUMMARY
# ==========================================

print("\n\n===================================")
print("DATA LOADING COMPLETE")
print("===================================")

print("\nDatasets loaded:")

for name, df in datasets.items():
    print(f"- {name}: {len(df)} rows")


# ==========================================
# 5. SHOW COMPOUNDS DATA
# ==========================================

if "compounds" in datasets:

    compounds = datasets["compounds"]

    print("\n\n===================================")
    print("COMPOUNDS DATA")
    print("===================================")

    print("\nColumn names:")
    print(compounds.columns.tolist())

    print("\nFirst 5 records:")
    print(compounds.head())