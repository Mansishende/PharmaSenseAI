import pandas as pd
from pathlib import Path


# ==========================================
# 1. FIND DATA FOLDER
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "synthetic_dataset"


# ==========================================
# 2. LOAD COMPOUNDS
# ==========================================

compounds = pd.read_csv(DATA_DIR / "compounds.csv")


# ==========================================
# 3. BASIC INFORMATION
# ==========================================

print("\n===================================")
print("PHARMASENSEAI DATA ANALYSIS")
print("===================================")


print("\nCOMPUNDS DATA")
print("-----------------------------------")

print("Number of compounds:", len(compounds))

print("\nColumns:")
print(compounds.columns.tolist())


# ==========================================
# 4. THERAPEUTIC AREAS
# ==========================================

print("\n===================================")
print("THERAPEUTIC AREAS")
print("===================================")

print(compounds["therapeutic_area"].value_counts())


# ==========================================
# 5. DISCOVERY PHASE
# ==========================================

print("\n===================================")
print("DISCOVERY PHASE")
print("===================================")

print(compounds["discovery_phase"].value_counts())


# ==========================================
# 6. CHEMICAL CLASSES
# ==========================================

print("\n===================================")
print("CHEMICAL CLASSES")
print("===================================")

print(compounds["chemical_class"].value_counts())


# ==========================================
# 7. TOXICITY
# ==========================================

print("\n===================================")
print("TOXICITY SCORE")
print("===================================")

print(compounds["toxicity_score"].describe())